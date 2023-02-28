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



## - for, sintaxis


## - desempaquetado en variable iteradora


## - enumerate, Ejer #23


## - recorrer distintas coleciones, str, set, dict, list


## - range


## - else, break, continue


## - Ejercicio #9