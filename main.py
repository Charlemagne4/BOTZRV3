from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.graphics import Color, RoundedRectangle
from kivy.core.window import Window

import requests
import json


from zr_settings import *
from secretPie import *
from colorama import init as colorama_init
import gspread
from gspread.cell import Cell
from itertools import chain



#initialize data
sa = gspread.service_account(filename="service_account.json")
sheet = sa.open("Mitchou M")
work_sheet = sheet.worksheet("Youcan-Orders")

data = {
        "Colis": []
        }
index_exc = 1
index = ""
index2 = ""
index_entered = []
stop_id = ""
colorama_init()
cells_to_update = []
numeros = []
numeros_added = []

def collectData(indexu, indexu2):
    Affichage = ""
    global index_exc, stop_id
    # fetching the data from the sheet based on the index
    try:
        value = list(work_sheet.get_values(f"A{indexu}:O{indexu2}"))
    except gspread.exceptions.APIError:
        Affichage = Affichage + "Wrong Number\n"
        return
    
    # multiple items loop
    for row in value:
        numeros.append(row[3])
        if len(row) < 15:
            for i in range(15 - len(row)):
                row.append("")
        # 000000000000000000000000000000
        # a,b,c,d,e,f,g,h,i,j,k,l,m =row

        if (row[9].strip() == "Confirmé") and (row[12].strip() != "Expedié"):

            # customizable reasons for various user errors 
            if indexu == indexu2:

                if row[9] != "Confirmé":
                    Affichage = Affichage + "You Client Didn't Confirm His Order, Wrong Number Or You Forget To Change It?\n"
                    return

            # filling numero
            number = str(row[3])
            numeros_added.append(number)
            number = number.zfill(10)

            # filling the name
            name = str(row[2])

            # filtering the product words
            product = str(row[6]) + "يسمح بفتح الطرد" + f" / RÉCLAMATION APPEL OU SMS AU {operator_num}"
            for item in filtered_words:
                if item[0] in product:
                    product = product.replace(item[0], item[1])

            # wilaya info
            wilaya = row[4].title().strip()
            

            # commune info
            commune = row[5].title().strip()

             # convert to 58 wilaya system
            if wilaya in checkable_wilaya:
                if commune in list(chain.from_iterable(list(convert_48_to_58.keys()))):
                    wilaya = next(v for k, v in convert_48_to_58.items() if commune in k)
                    
            # filling total sum
            prod_price = float(row[8])
            try:
                tot_price = prod_price + float(row[11])
            except TypeError:
                try:
                    tot_price = prod_price + int(wilayaStats[wilaya]["Stopdesk"]) if row[
                                                                                10].strip() == "Stop desk" else prod_price + \
                                                                                                                int(wilayaStats[
                                                                                                                    wilaya]["Domicile"])
                except TypeError:
                    if row[10].strip() == "Stop desk":
                        Affichage += f"Stop Desk indisponible sur ligne {indexu + value.index(row)}\n"
                    else:
                        Affichage += f"Domicile indisponible {indexu + value.index(row)}\n"
            except ValueError:
                try:
                    if row[10].strip() == "Stop desk":
                        tot_price = prod_price + int(wilayaStats[wilaya]["Stopdesk"])
                    else:
                        tot_price = prod_price + int(wilayaStats[wilaya]["Domicile"])
                except TypeError:
                    if row[10].strip() == "Stop desk":
                        Affichage += f"Stop Desk indisponible sur ligne {indexu + value.index(row)}\n"
                    else:
                        Affichage += f"Domicile indisponible {indexu + value.index(row)}\n"
                    continue

           

            # adding the info to the sheet
            instanceOfColis = {
                "Tracking": "",
                "TypeLivraison": "1" if row[10].strip() == "Stop desk" else "0",
                "TypeColis": "1" if row[14].strip().lower() == "x" else "0",
                "Confrimee": "",
                "Client": f"{prefix} {name}",
                "MobileA": number,
                "MobileB": "",
                "Adresse": "",
                "IDWilaya": str(wilayaStats[wilaya]["IDWilaya"]),
                "Commune": commune,
                "Total": tot_price,
                "Note": row[13],#Note row in sheet
                "TProduit": product,
                "id_Externe": prefix,
                "Source": ""
            } 
            # print(instanceOfColis["IDWilaya"])
            data["Colis"].append(instanceOfColis)
            # data = [prefix + " " + name, number, "", product, "1", commune, wilaya, commune, tot_price, row[13], prefix,
            #         "OUI" if row[14].strip().lower() == "x" else "h",
            #         "OUI" if row[10].strip() == "Stop desk" else ""]
            # ws.write_row(index_exc, 0, data)

            # to set the command to expidé later
            cells_to_update.append(Cell(row=indexu + value.index(row), col=13, value="Expedié"))

            # this index has been successfully entered

            if (indexu == indexu2):
                index_entered.append(indexu)
                Affichage = Affichage + f"Command {indexu} Entered\n"
            else:
                index_entered.append(indexu + value.index(row))
                Affichage = Affichage + f"Command {indexu + value.index(row)} Entered\n"

            index_exc += 1

        elif indexu == indexu2:
            Affichage = Affichage + f"Command Is Not Confirmed Or Is Already Expidé\n"
            continue

    Affichage = Affichage + f"You're About To Send {len(index_entered)} Order(s)\n"
    return Affichage

def SendData():
    Affichage = ""
    url = "https://procolis.com/api_v1/add_colis"
    headers = {
        "token": token,
        "key": key
    }

    try:
        response = requests.post(url, headers=headers, json=data)  # Le paramètre json envoie le body en raw JSON
        response.raise_for_status()
        Affichage += "Statut:", response.status_code
        
        if(response.status_code >= 200 & response.status_code < 300):
            
            try:
                
                response_json = response.json()
                
            
            except json.JSONDecodeError:
                Affichage += "Erreur: La réponse n'est pas en format JSON"
                Affichage += "Contenu brut:", response.text
            for colis in response_json['Colis']:
                    if(colis['MessageRetour']!= 'Good'):
                        Affichage += f'{colis['MessageRetour']} {colis['Client']} {colis['IDWilaya']}' 
            #update Sheet
            work_sheet.update_cells(cells_to_update)
    
    except requests.exceptions.HTTPError as http_err:
        Affichage += f"Erreur HTTP: {http_err}"
    except Exception as err:
        Affichage += f"Autre erreur: {err}"
        
    return Affichage

class MyApp(App):
    
    
    
    def build(self):
        # Set up the layout
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # Set background color to Discord-like dark theme
        Window.clearcolor = (0.12, 0.13, 0.15, 1)  # Discord dark background color

        # Add a custom header with Discord font styling
        header = Label(text="UNHINGED ZR Bot", font_size=32, color=(1, 1, 1, 1), size_hint_y=None, height=50, bold=True)
        layout.add_widget(header)

        # Create TextInput widgets for input with Discord-like style
        self.input1 = self.create_text_input('Enter first number')
        self.input2 = self.create_text_input('Enter second number')

        # Create a Label to display the result with Discord-like styling
        self.result_label = Label(text="Result will be shown here", font_size=24, color=(1, 1, 1, 1), halign="center", valign="middle", size_hint_y=None, height=100)
        self.result_label.bind(size=self.result_label.setter('text_size'))

        # Create Buttons for addition and subtraction with Discord style
        button_add = self.create_button("Add", self.collect)
        button_subtract = self.create_button("Subtract", self.Send)

        # Add widgets to the layout
        layout.add_widget(self.input1)
        layout.add_widget(self.input2)
        layout.add_widget(button_add)
        layout.add_widget(button_subtract)
        layout.add_widget(self.result_label)

        return layout

    def create_text_input(self, hint):
        text_input = TextInput(hint_text=hint, input_filter='float', font_size=18, size_hint_y=None, height=50, background_color=(0.2, 0.22, 0.27, 1), foreground_color=(1, 1, 1, 1), padding_y=[12, 12])
        with text_input.canvas.before:
            Color(0.2, 0.22, 0.27, 1)  # Discord input background color
            text_input.border = (0, 0, 0, 0)
            RoundedRectangle(pos=text_input.pos, size=text_input.size, radius=[10])
        return text_input

    def create_button(self, text, callback):
        button = Button(text=text, font_size=22, size_hint_y=None, height=50, background_color=(0.55, 0.58, 0.64, 1), color=(1, 1, 1, 1), border=(0, 0, 0, 0))
        button.bind(on_press=callback)
        with button.canvas.before:
            Color(0.55, 0.58, 0.64, 1)  # Discord button background color
            RoundedRectangle(pos=button.pos, size=button.size, radius=[10])
        return button
    
    def collect(self, instance):
        # Get the values from the TextInputs
        try:
            num1 = int(self.input1.text)
            num2 = int(self.input2.text)
            inputs = [num1]
            for idx, value in enumerate(inputs, start=1):
            # Check if value is empty
                if not value:
                    print(f"Index {idx} is empty.")
                    return False
            
                # Check if value is an integer
                try:
                    value = int(value)
                except ValueError:
                    print(f"\nIndex {idx} is not a valid integer.")
                    return False
                
                # Print valid integer (optional)
                print(f"\nIndex {idx} is a valid integer: {value}")
        
        # If all checks pass
            print("Both indices are valid integers.\n")
            affichageFinal = collectData(num1,num2)
            self.result_label.text = f"{affichageFinal}"
            return True
        except ValueError:
            self.result_label.text = "Please enter valid numbers\n"
            affichageFinal = collectData(num1,num1)
            self.result_label.text = f"{affichageFinal}"
        
        
            
    
    def Send(self, instance):
        # Sending DATA
        affichageFinal = SendData()
        self.result_label.text = f"{affichageFinal}"

if __name__ == "__main__":
    MyApp().run()
