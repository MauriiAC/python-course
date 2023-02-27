## - Sintaxis
personas = {
    "name": "Mauricio", 
    "edad": 32, 
    "mail": "mauricio@gmail.com"
  }

persona2 = {
    "name": "Lionel", 
    "edad": 35, 
    "mail": "lio_10@gmail.com"
  }

## - Recuperar un valor
# print(persona1["mail"])

# ## - Mutabilidad
# persona1["mail"] = "mauricio_91@gmail.com"
# # print(persona1)
# persona1["edad"] += 1
# print(persona1)


## - Funciones integradas
# persona1 = {
#     "name": "Mauricio", 
#     "edad": 32, 
#     "mail": "mauricio@gmail.com"
#   }

# del persona1["edad"]

# print("name" in persona1)

# persona1.pop("name")

# print(persona1)

# persona1["edad"] = 25
# persona1["city"] = "Barcelona"

# persona1.update({
#     "city":" Barcelona",
#     "phone": 123456,
#     "weight": 70
# })

# persona1.update([("city"," Barcelona"), ("phone", 123456), ("weight", 70)])

# print(persona1)

# print(len(persona1))

## -  Ejercicios #8 a #10

# 8
# Dada la lista 'personas' (mockups.py) devolver la cantidad de generos diferentes que hay

personas = [
    {"id":1,"first_name":"Catha","last_name":"Carlton","city":"Qingshandi","email":"ccarlton0@twitter.com","gender":"Polygender"},
    {"id":2,"first_name":"Toddie","last_name":"Ibeson","city":"San Juan","email":"tibeson1@freewebs.com","gender":"Bigender"},
    {"id":3,"first_name":"Ashlee","last_name":"McAuslan","city":"São Jerônimo","email":"amcauslan2@pcworld.com","gender":"Polygender"},
    {"id":4,"first_name":"Julie","last_name":"Fischer","city":"Lasusua","email":"jfischer3@ucoz.com","gender":"Agender"},
    {"id":5,"first_name":"Manda","last_name":"Mapis","city":"Sindang","email":"mmapis4@foxnews.com","gender":"Non-binary"},
    {"id":6,"first_name":"Noami","last_name":"Rubanenko","city":"Siemianowice Śląskie","email":"nrubanenko5@geocities.com","gender":"Genderfluid"},
    {"id":7,"first_name":"Daffi","last_name":"Wherton","city":"Kamirenjaku","email":"dwherton6@privacy.gov.au","gender":"Bigender"},
    {"id":8,"first_name":"Tamma","last_name":"Worsham","city":"Batang","email":"tworsham7@globo.com","gender":"Male"},
    {"id":9,"first_name":"Gibby","last_name":"Blacktin","city":"Makarov","email":"gblacktin8@mac.com","gender":"Agender"},
    {"id":10,"first_name":"Locke","last_name":"Pirdy","city":"Ketanggungan","email":"lpirdy9@wix.com","gender":"Polygender"},
    {"id":11,"first_name":"Dorree","last_name":"Claypool","city":"Laborie","email":"dclaypoola@un.org","gender":"Female"},
    {"id":12,"first_name":"Jermaine","last_name":"Duplan","city":"Chemin Grenier","email":"jduplanb@skype.com","gender":"Polygender"},
    {"id":13,"first_name":"Kliment","last_name":"Divill","city":"Baochang","email":"kdivillc@tamu.edu","gender":"Agender"},
    {"id":14,"first_name":"Bernice","last_name":"O'Hartnett","city":"Askainen","email":"bohartnettd@tripod.com","gender":"Genderqueer"},
    {"id":15,"first_name":"Teirtza","last_name":"Summerlee","city":"Babakanbungur","email":"tsummerleee@scientificamerican.com","gender":"Agender"}
    ]

# gender = set()

# gender.add(personas[0]["gender"])
# gender.add(personas[1]["gender"])
# gender.add(personas[2]["gender"])
# gender.add(personas[3]["gender"])
# gender.add(personas[4]["gender"])
# gender.add(personas[5]["gender"])
# gender.add(personas[6]["gender"])
# gender.add(personas[7]["gender"])
# gender.add(personas[8]["gender"])
# gender.add(personas[9]["gender"])
# gender.add(personas[10]["gender"])
# gender.add(personas[11]["gender"])
# gender.add(personas[12]["gender"])
# gender.add(personas[13]["gender"])
# gender.add(personas[14]["gender"])


gender=set()
for person in personas:
    gender.add(person["gender"])
# print(gender)

print(len(gender))