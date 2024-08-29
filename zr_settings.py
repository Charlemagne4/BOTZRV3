# filtered words for the sake of being professional
# the first word is replaced by the second
filtered_words = [["timsah 🐊", "lacoste"],
                  ["🔥 NiiKKEE 🔥", "Nike"],
                  ["🐊🔥🐊", "lacoste"],
                  ["Rose", "Saumon"],
                  ["rose", "Saumon"],
                  ["🐊 🔥", " "],
                  ["🐊🔥🐊"," "],
                  ["💥💥"," "]]

# either write firefox or chrome exactly like that, doing otherwise would crash the program
browser = "firefox".lower()


convert_48_to_58 = {("Charouine", "Ouled Aïssa", "Talmine", "Ouled Saïd", "Timimoun", "Ksar Kaddour", "Tinerkouk",
                     "Aougrout", "Deldoul", "Metarfa"): "Timimoun",
                    ("Bordj Badji Mokhtar", "Timiaouine"): "Bordj Badji Mokhtar",
                    ("Ech Chaïba", "Doucen", "Ouled Djellal", "Besbes", "Ras El Miaad", "Sidi Khaled"): "Ouled Djellal",
                    ("Ksabi", "Ouled Khoudir", "Béni Abbès", "Tamtert", "Igli", "El Ouata", "Beni Ikhlef", "Kerzaz",
                     "Timoudi"): "Béni Abbès",
                    ("In Ghar", "In Salah", "Foggaret Ezzaouia"): "In Salah",
                    ("In Guezzam", "Tin Zaouatine"): "In Guezzam",
                    ("Nezla", "Tebesbest", "Touggourt", "Zaouia El Abidia", "El Allia", "El Hadjira", "Benaceur",
                     "M'Naguer", "Taibet", "Blidet Amor", "Tamacine", "Megarine", "Sidi Slimane"): "Touggourt",
                    ("Bordj El Haouas", "Djanet"): "Djanet",
                    ("M'Rara", "Sidi Amrane", "Tendla", "El M'Ghair", "Oum Touyour", "Sidi Khellil", "Still",
                     "Djamaa"): "M'Ghair",
                    ("El Menia", "Hassi Gara", "Hassi Fehal"): "Meniaa"}

checkable_wilaya = ('Adrar', 'Biskra', 'Béchar', 'Tamanrasset', 'Ouargla', 'Illizi', 'El Oued', 'Ghardaïa')




wilayaStats= {
  "Adrar":{
    "IDWilaya": "01",
    "Domicile": "1400",
    "Stopdesk": "900",
    "Annuler": "200"
  },
  "Chlef":{
    "IDWilaya": "02",
    "Domicile": "750",
    "Stopdesk": "450",
    "Annuler": "200"
  },
  "Laghouat":{
    "IDWilaya": "03",
    "Domicile": "950",
    "Stopdesk": "600",
    "Annuler": "200"
  },
  "Oum El Bouaghi":{
    "IDWilaya": "04",
    "Domicile": "800",
    "Stopdesk": "450",
    "Annuler": "200"
  },
  "Batna":{
    "IDWilaya": "05",
    "Domicile": "800",
    "Stopdesk": "450",
    "Annuler": "200"
  },
  "Béjaïa":{
    "IDWilaya": "06",
    "Domicile": "800",
    "Stopdesk": "450",
    "Annuler": "200"
  },
  "Biskra":{
    "IDWilaya": "07",
    "Domicile": "950",
    "Stopdesk": "600",
    "Annuler": "200"
  },
  "Béchar":{
    "IDWilaya": "08",
    "Domicile": "1100",
    "Stopdesk": "650",
    "Annuler": "200"
  },
  "Blida":{
    "IDWilaya": "09",
    "Domicile": "400",
    "Stopdesk": "300",
    "Annuler": "200"
  },
  "Bouira":{
    "IDWilaya": 10,
    "Domicile": "750",
    "Stopdesk": "450",
    "Annuler": "200"
  },
  "Tamanrasset":{
    "IDWilaya": 11,
    "Domicile": "1600",
    "Stopdesk": "1050",
    "Annuler": "250"
  },
  "Tébessa":{
    "IDWilaya": 12,
    "Domicile": "850",
    "Stopdesk": "450",
    "Annuler": "200"
  },
  "Tlemcen":{
    "IDWilaya": 13,
    "Domicile": "850",
    "Stopdesk": "500",
    "Annuler": "200"
  },
  "Tiaret":{
    "IDWilaya": 14,
    "Domicile": "800",
    "Stopdesk": "450",
    "Annuler": "200"
  },
  "Tizi Ouzou":{
    "IDWilaya": 15,
    "Domicile": "750",
    "Stopdesk": "450",
    "Annuler": "200"
  },
  "Alger":{
    "IDWilaya": 16,
    "Domicile": "500",
    "Stopdesk": "350",
    "Annuler": "200"
  },
  "Djelfa":{
    "IDWilaya": 17,
    "Domicile": "950",
    "Stopdesk": "600",
    "Annuler": "200"
  },
  "Jijel":{
    "IDWilaya": 18,
    "Domicile": "800",
    "Stopdesk": "450",
    "Annuler": "200"
  },
  "Sétif":{
    "IDWilaya": 19,
    "Domicile": "750",
    "Stopdesk": "450",
    "Annuler": "200"
  },
  "Saïda":{
    "IDWilaya": 20,
    "Domicile": "800",
    "Stopdesk": None,
    "Annuler": "200"
  },
  "Skikda":{
    "IDWilaya": 21,
    "Domicile": "800",
    "Stopdesk": "450",
    "Annuler": "200"
  },
  "Sidi Bel Abbès":{
    "IDWilaya": 22,
    "Domicile": "800",
    "Stopdesk": "450",
    "Annuler": "200"
  },
  "Annaba":{
    "IDWilaya": 23,
    "Domicile": "800",
    "Stopdesk": "450",
    "Annuler": "200"
  },
  "Guelma":{
    "IDWilaya": 24,
    "Domicile": "800",
    "Stopdesk": "450",
    "Annuler": "200"
  },
  "Constantine":{
    "IDWilaya": 25,
    "Domicile": "800",
    "Stopdesk": "450",
    "Annuler": "200"
  },
  "Médéa":{
    "IDWilaya": 26,
    "Domicile": "750",
    "Stopdesk": "450",
    "Annuler": "200"
  },
  "Mostaganem":{
    "IDWilaya": 27,
    "Domicile": "800",
    "Stopdesk": "450",
    "Annuler": "200"
  },
  "M'Sila":{
    "IDWilaya": 28,
    "Domicile": "850",
    "Stopdesk": "500",
    "Annuler": "200"
  },
  "Mascara":{
    "IDWilaya": 29,
    "Domicile": "800",
    "Stopdesk": "450",
    "Annuler": "200"
  },
  "Ouargla":{
    "IDWilaya": 30,
    "Domicile": "950",
    "Stopdesk": "600",
    "Annuler": "200"
  },
  "Oran":{
    "IDWilaya": 31,
    "Domicile": "800",
    "Stopdesk": "450",
    "Annuler": "200"
  },
  "El Bayadh":{
    "IDWilaya": 32,
    "Domicile": "1100",
    "Stopdesk": "600",
    "Annuler": "200"
  },
  "Illizi":{
    "IDWilaya": 33,
    "Domicile": None,
    "Stopdesk": None,
    "Annuler": None
  },
  "Bordj Bou Arreridj":{
    "IDWilaya": 34,
    "Domicile": "750",
    "Stopdesk": "450",
    "Annuler": "200"
  },
  "Boumerdès":{
    "IDWilaya": 35,
    "Domicile": "750",
    "Stopdesk": "450",
    "Annuler": "200"
  },
  "El Tarf":{
    "IDWilaya": 36,
    "Domicile": "800",
    "Stopdesk": "450",
    "Annuler": "200"
  },
  "Tindouf":{
    "IDWilaya": 37,
    "Domicile": None,
    "Stopdesk": None,
    "Annuler": None
  },
  "Tissemsilt":{
    "IDWilaya": 38,
    "Domicile": "800",
    "Stopdesk": None,
    "Annuler": "200"
  },
  "El Oued":{
    "IDWilaya": 39,
    "Domicile": "950",
    "Stopdesk": "600",
    "Annuler": "200"
  },
  "Khenchela":{
    "IDWilaya": 40,
    "Domicile": "800",
    "Stopdesk": None,
    "Annuler": "200"
  },
  "Souk Ahras":{
    "IDWilaya": 41,
    "Domicile": "800",
    "Stopdesk": "450",
    "Annuler": "200"
  },
  "Tipaza":{
    "IDWilaya": 42,
    "Domicile": "750",
    "Stopdesk": "450",
    "Annuler": "200"
  },
  "Mila":{
    "IDWilaya": 43,
    "Domicile": "800",
    "Stopdesk": "450",
    "Annuler": "200"
  },
  "Aïn Defla":{
    "IDWilaya": 44,
    "Domicile": "750",
    "Stopdesk": "450",
    "Annuler": "200"
  },
  "Naâma":{
    "IDWilaya": 45,
    "Domicile": "1100",
    "Stopdesk": "600",
    "Annuler": "200"
  },
  "Aïn Témouchent":{
    "IDWilaya": 46,
    "Domicile": "800",
    "Stopdesk": "450",
    "Annuler": "200"
  },
  "Ghardaïa":{
    "IDWilaya": 47,
    "Domicile": "950",
    "Stopdesk": "600",
    "Annuler": "200"
  },
  "Relizane":{
    "IDWilaya": 48,
    "Domicile": "800",
    "Stopdesk": "450",
    "Annuler": "200"
  },
  "Timimoun":{
    "IDWilaya": 49,
    "Domicile": "1400",
    "Stopdesk": None,
    "Annuler": "200"
  },
  "Bordj Badji Mokhtar":{
    "IDWilaya": 50,
    "Domicile": None,
    "Stopdesk": None,
    "Annuler": None
  },
  "Ouled Djellal":{
    "IDWilaya": 51,
    "Domicile": "950",
    "Stopdesk": "600",
    "Annuler": "200"
  },
  "Béni Abbès":{
    "IDWilaya": 52,
    "Domicile": "1000",
    "Stopdesk": None,
    "Annuler": "200"
  },
  "In Salah":{
    "IDWilaya": 53,
    "Domicile": "1600",
    "Stopdesk": None,
    "Annuler": "250"
  },
  "In Guezzam":{
    "IDWilaya": 54,
    "Domicile": "1600",
    "Stopdesk": None,
    "Annuler": "250"
  },
  "Touggourt":{
    "IDWilaya": 55,
    "Domicile": "950",
    "Stopdesk": "600",
    "Annuler": "200"
  },
  "Djanet":{
    "IDWilaya": 56,
    "Domicile": None,
    "Stopdesk": None,
    "Annuler": None
  },
  "M'Ghair":{
    "IDWilaya": 57,
    "Domicile": "950",
    "Stopdesk": None,
    "Annuler": "200"
  },
  "Meniaa":{
    "IDWilaya": 58,
    "Domicile": "1000",
    "Stopdesk": None,
    "Annuler": "200"
  }
}