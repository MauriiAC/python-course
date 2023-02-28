## - Flujo de control
# https://juegosrobotica.es/wp-content/uploads/diagrama-de-flujo-cafe.jpg


## - Sintaxis del condicional
# nombre = "Ana"

# if len(nombre) > 5:
#     print("Su nombre es largo")
#     print("otra impresión")
# if nombre[0] == "A":
#     print("Su nombre empieza con A")
# if nombre == nombre.capitalize():
#     print("Su nombre está bien escrito")

## - Anidamiento

# nombre = "Ana"

# if len(nombre) > 5:
#   print("Su nombre es largo")
#   print("otra impresión")
#   if nombre[0] == "A":
#       print("Su nombre empieza con A")
# if nombre == nombre.capitalize():
#   print("Su nombre está bien escrito")


## - elif, else
# edad = int(input("Ingrese su edad: "))

# if edad < 18:
#     print("Tienes una vida por delante..")
# elif edad < 30:
#     print("Trabaja duro por tu futuro")
# elif edad < 60:
#     print("Disfruta lo que has logrado")
# else:
#     print("Que bueno seguir compartiendo contigo")

# ## - autocasting
# nombre = input("Ingrese su nombre: ")

# if nombre:
#     print(f'Hola {nombre}')
# else:
#     print("No ingresaste ningún nombre")

# ## - condiciones con operadores lógicos
# nombre = input("Ingrese su nombre: ")

# if nombre and len(nombre) > 4 or nombre[0] == 'Z':
#     print(f'Hola {nombre}')
# else:
#     print("No ingresaste ningún nombre")

# ## - pass
# nombre = input("Ingrese su nombre: ")

# if nombre:
#     # TO DO: preguntar que hacer acá
#     pass

# print("Resto de mi programa...")

## - Ejercicios #11 al #15
# # 12  
# # Pedir al usuario que ingrese una palabra y devolver un msj diciendo si la misma es capicua o no

# palabra = input("Ingrese una palabra: ")

# palabra = palabra.lower()

# if palabra == palabra[::-1]:
#     print("su palabra es capicua")
# else:
#     print("su palabra NO es capicua")




# 14  
# Pedir al usuario que ingrese un número
# Si el número es divisible por 3 imprimir {"El número es divisible por 3"} 
# Si el número es divisible por 7 imprimir {"El número es divisible por 7"} 
# Si el número es divisible por 3 y por 7 a la vez imprimir {"El número es divisible por 3 y por 7"}
# Si el número no es divisible ni por 3 ni por 7 imprimr {"El número no es divisible ni por ni por 7"}

# numero = int(input("Ingrese un numero: "))

# if numero % 3 == 0 and numero % 7 == 0:
#     print("El numero es divible por 3 y por 7")
# elif numero % 3 == 0:
#     print("El numero es divisible por 3")
# elif numero % 7 == 0:
#     print("El numero es divisible por 7")
# else:
#     print("Su numero no es divisible ni por 3 ni por 7")

# 15  
# Dada la tupla r3 de mockups.py, pedir al usuario que ingrese un nombre de una ciudad, devolver si se encuentra en la primer o segunda mitad de la tupla, según el indice que define su posición.
# Si se encuentra exactamente en el medio, imprimir {"Se encuentra en el medio de la tupla"}
# Si la ciudad no se encuentra en el listado, imprimir {"No se encuentra {nombre ciudad} en la lista"}


ciudades = (
    "San Jorge", "Quitilipi", "Granadero Baigorria", "Alderetes", "Gualeguay", "Chimbas", "Rada Tilly", "Cote-Lai", "Elena", "Yerba Buena", "Laboulaye", "La Rioja", "Castelli", "Aminga", "Isla Verde", "Pirane", "General Enrique Godoy", "Alumine", "Rio Pico", "Sampacho", "Villa de Soto", "Embarcacion", "Caseros", "Jesus Maria", "Salta", 
    "Esquina", 
    "Puerto Iguazu", "Mercedes", "Castelli", "Cinco Saltos", "El Bolson", "Tamberias", "Guernica", "Doblas", "Villa Santa Rita", "Mercedes", "Carlos Casares", "Vera", "Zapala", "Santa Ana", "Libertador General San Martin", "Villa Maria", "Basail", "Gualeguay", "Villa La Angostura", "Basail", "San Lorenzo", "Tostado", "Libertad", "General Conesa", "General Pico"
    )

ciudad = input("Ingrese una ciudad: ")

mitad = (len(ciudades)-1)/2

if ciudad in ciudades:
  pos = ciudades.index(ciudad)    

if pos < mitad:
    print(f'{ciudad} está en la primera mitad tabla')
elif pos == mitad:
    print(f'{ciudad} está en la mitad de la tabla')
else:
    print(f'{ciudad} está en la segunda mitad')

