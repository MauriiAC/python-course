## - Concepto de variable - graficar

# ## - Sintaxis
# edad = 30
# print(edad)

# ## - Tipo de dato de la variable
# a = "Mauricio"
# print(type(a))
# b = 5
# print(type(b))


## - Ejemplo con distintos tipos
# nombre = "Mauricio"
# edad = 32

# print("Hola " + nombre)
# print(edad + 1)

# print("Hola " + nombre + " tienes " + str(edad) + " años.")

# - Asignación anidada
# nombre = "Mauricio"
# apellido = "Cuello"

# nombre_completo = nombre + " " + apellido
# saludo = "Hola " + nombre_completo + "!"

# print(saludo)

# ## - NameError
# nombre = "Mauricio"
# print(nombre)

# ## - Buenas practicas en nombres
# # case sensitive
# nombre_cliente_1 = "Mauricio"
# Nombre_cliente_1 = "Ana"


# ## - Input
# nombre = input("Ingrese su nombre: ")
# print("Hola " + nombre)

# ## - Parseo/Casteo
# nombre = input("Ingrese su nombre: ")
# edad = input("Ingrese su edad: ")

# print("Hola " + nombre + " el año que viene tendrás " + str(int(edad)+1) + " años.")


# ## - prefixer f-string
# nombre = input("Ingrese su nombre: ")
# edad = int(input("Ingrese su edad: "))

# print(f"Hola {nombre} el año que viene tendrás {edad+1} años.")

## Ejercicios #1 al #3
#3 Pedir al usuario que ingrese su nombre, precio por hora y horas trabajadas y devuelva el pago que le corresponde
nombre = input("Ingrese su nombre: ")
valor_hora = int(input("Ingrese su valor_hora: "))
horas_trabajadas = int(input("Ingrese su horas_trabajadas: "))


print(f'Hola {nombre}, tu pago es {valor_hora * horas_trabajadas}')
