## - Necesidad de su uso
# n = int(input("Ingrese el limite: "))

# if 1 < n:
#     print(1)
# if 2 < n:
#     print(2)

## - while, sintaxis
# n = int(input("Ingrese el limite: "))
# i = 1

# while i < n:
#     print('imprimimos el valor de i')
#     print(i)
#     i += 1

# ## - uso, caso indeterminado
# contrasena = 'Homero123'

# valor_ingresado = input("Ingrese su contraseña: ")

# while valor_ingresado != contrasena:
#   valor_ingresado = input("Contraseña incorrecta, intente de nuevo: ")

# print("Bienvenido!")

# ## - break, else, continue
# numero = int(input("Ingrese un numero: "))
# i = 1

# while i < numero:
#     if i > 10:
#         break
#     print(i)
#     i += 1
# else:
#     print("Se imprimieron todos los numeros")

# print("Se finalizó el programa")


## Ejercicios Ejercicios #8 a #10 y #16 a #20
# 16
# Escribir un programa donde el usuario tiene que adivinar un número, si adivina, imprimir el mensaje "Advinaste", si no lo logra darle otra oportunidad hasta llegar a 3 oportunidades, en caso que no adivine imprimir "Se te acabaron las oportunidades" - Usar while-else

# numero = int(input("Ingrese un numero: "))
# intentos = 1
# numero_secreto = 5

# while numero != numero_secreto:
#     if intentos == 3:
#         print("Se te acabaron los intentos")
#         break
#     else:
#       numero = int(input("Ingrese otro numero: "))
#       intentos += 1
# else:
#   print("Adivinaste!")
        
# print("Se finalizó el programa")

# 17  
# Escribir un programa que pregunte al usuario números hasta que ingrese el 0, en ese momento devolver la suma de todos los números ingresados

# numero = int(input("Ingrese un numero: "))
# contador = 0

# while numero != 0:
#     contador += numero
#     numero = int(input("Ingrese otro numero: "))

# print(contador)

# # 18  
# # Escribir un progama que pida al usuario valores hasta que ingrese el 0, devolver la suma de los números ingresados pero sin tener en cuenta los números que sean divisibles por 3 - usar continue

# numero = int(input("Ingrese un numero: "))
# contador = 0

# while numero != 0:
#     if numero % 3 == 0:
#         numero = int(input("Ingrese otro numero: "))
#         continue
#     contador += numero
#     numero = int(input("Ingrese otro numero: "))

# print(contador)

# 10  
# Dado el diccionario "respuestas", escribir un programa que saque por pantalla el mensaje "chat activo: " y según lo que el usuario ingrese devolver el valor correspondiente a esa clave, si la clave no existe imprimr 'lo siento, no te entendí, me lo dices de otra forma?'
# Finalizar el chat si el segundo valor de la tupla es True
respuestas = {
    'hola chatbot': ('hola, como estás?', False),
    'buen dia': ('muy buenos días, espero te encuentres muy bien', False),
    'adios': ('hasta la próxima compañero', True),
    'cuanto es 2 + 2?': (4, False)
}

# print("Chat activo:")
# pregunta = input("> ")

# # nos aseguramos que el primer input sea valido
# while pregunta not in respuestas:
#     print("'lo siento, no te entendí, me lo dices de otra forma?'")
#     pregunta = input("> ")

# # algoritmo principal
# while (respuestas[pregunta][1] != True):
#     print(respuestas[pregunta][0])
#     pregunta = input("> ")
#     while pregunta not in respuestas:
#         print("'lo siento, no te entendí, me lo dices de otra forma?'")
#         pregunta = input("> ")
# else:
#     # decimos adios
#     print(respuestas[pregunta][0])

# texto = input('Chat activo: ')
# while True:
#     respuesta = respuestas.get(texto)
#     if respuesta:
#         if respuesta[1]:
#             print(respuesta[0])
#             break
#         print(respuesta[0])
#         texto = input(">> ")
#     else:
#         texto = input("Lo siento, no te entendi, me lo dices de otra forma?")

# ## - for, sintaxis

# lista = [1,2,3,4,5]
# lista_dobles = []

# for i in lista:
#     lista_dobles.append(i*2)

# print(lista_dobles)

# ## - desempaquetado en variable iteradora, r4
# lista_personas = [("Mauricio", "Cuello", 30), ("Lionel", "Messi", 34), ("Cristiano", "Ronaldo", 34), ("Pepe", "Mujica", 40)]

# for nombre, apellido, edad in lista_personas:
#     print(nombre)
#     print(edad)


## - enumerate, Ejer #23
# 23 
# Dada la lista de paises dentro de mockups.py armar un programa que obtenga la posición del pais con el nombre más largo

# paises = ['Canada', 'USA', 'Mexico', 'Australia', 'Argentina', 'Corea del Sur', 'China', 'India', 'Singapur', 'Croacia']
# # print(list(enumerate(paises)))

# candidato = paises[0]
# pos_candidato = 0

# for pos, pais in enumerate(paises):
    
#     if len(pais) > len(candidato):
#         candidato = pais
#         pos_candidato = pos

# print(pos_candidato)

## - recorrer distintas coleciones, str, set, dict, list

# for i in "Mauricio":
#     print(i)

## - range

# for i in range(5, 15, 2):
#     print(i)


# ## - else, break, continue
# mi_lista = [3,5,90,12,11]

# for i in mi_lista:
#     if i == 9:
#         break
# else:
#     print("No hay ningún 9")

# print("Se finalizó el programa")

## - Ejercicio #9
# 9
# Dada la lista personas en mockups.py, pedir al usuario que ingrese una letra y devolver 
# una lista con los nombres de las personas que su nombre empieza con esa letra
# En el caso que no haya ninguno, devolver que no existe ningún nombre con esa letra 
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

letra = input("Ingrese una letra: ")
nombres = set()

for persona in personas:
    if letra.capitalize() == persona["first_name"][0]:
        nombres.add(persona["first_name"])

if len(nombres) > 0:
  print(list(nombres))
else:
  print("No existe un nombre con esa letra")