## - Tipos de fallos: errores, excepciones

## - Sintacticos
# print("Hola a todos")

# print("Espero estén disfrutando este curso)

# if 5<3
#   print("5 es mayor a 3")

# print("Chau"

## - Excepciones, runtime
# print("Hola a todos")

# name = "Mauricio"
# # if len(name) > 4:
# #   print(f'Hola {Name}')
# # [].pop()
# # mi_lista = [1,2,3]
# # print(mi_lista[len(mi_lista)])

# edad = input("Ingrese su edad: ")

# print('El año que viene tendrás ' + str(int(edad)+1) + ' años.')

# print("Ejecutando otras cosas importantes")


## - Comprobaciones para evitar errores

# mi_lista = [10,20,30,40]

# n = int(input("Ingrese la cant de elem a extraer: "))

# for i in range(n):
#   if len(mi_lista) > 0:
#     print(mi_lista.pop())


## - Capturar errores

# try:
#   nombre = input("Ingrese su nombre: ")
#   edad = int(input("Ingrese su edad: "))
#   print(f'Hola {nombre}, el año que viene tendrás {edad+1} años')
# except:
#   print("No ingresaste una edad en formato numero")

# print("Ejecutando otras cosas importantes")

## - else, finally, varias excepciones, aserciones custom

# def imc(peso, altura):
#   assert altura > 0, "La altura debe ser un numero mayor a 0"
#   assert peso > 0, "el peso debe ser un numero mayor a 0"
#   return peso / (altura**2)

# while True:
#   try:
#     peso = float(input("Ingrese su peso: "))
#     altura = float(input("Ingrese su altura: "))
#     valor_imc = imc(peso, altura)
#     print(valor_imc)
#   except ValueError as e:
#     print("El formato de la altura y el peso debe ser numerico")
#   except ZeroDivisionError as e:
#     print("La altura no puede ser 0")
#   except AssertionError as e:
#     print(e)
#   except Exception as e:
#     print(type(e))
#     print("Ingresó valores incorrectos")
#   else:
#     print("Se finalizó sin fallos")
#     break
#   finally:
#     print("Se finalizó un intento")

# print("Ejecutando otras cosas importantes")
## - aserciones custom

