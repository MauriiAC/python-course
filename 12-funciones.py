## - integradas vs propias
# print(type(len("Mauricio")))

# ## - sintaxis
# def saluda():
#     print("Buenos días!")

# ## - definición vs invocación
# saluda()

## - reutilización de código 
## - uso de parametros
## - generalización

# def calcula(op, a, b):
#   if op == 'sum':
#     print(f'El resultado de sumar {a} + {b}: {a+b}')
#   elif op == 'res':  
#     print(f'El resultado de restar {a} - {b}: {a-b}')
#   elif op == 'mul':
#     print(f'El resultado de multiplicar {a} * {b}: {a*b}')
#   elif op == 'div':
#     print(f'El resultado de dividir {a} / {b}: {a/b}')


# print("Haciendo algunas cosas...")

# calcula('sum',2,11)

# print("haciendo mas cosas importantes...")

# calcula('res', 7, 2)

# calcula('mul',3,8)



# ## - return
# def calcula(op, a, b):
#   if op == 'sum':
#     return a + b
#     print("Se sumaro los valores") # No se lee porque el return finaliza la ejecución
#   elif op == 'res':  
#     return a - b
#   elif op == 'mul':
#     return a * b
#   elif op == 'div':
#     return a / b
  
# print(calcula('sum', 2,8))

# ## - ambito de variable (scope a nivel de función)
# nombre = "Jorge"

# def saluda_con_nombre():
#     nombre = "Mauricio"
#     return f'Hola {nombre}'

# print(saluda_con_nombre())

# print(nombre)

# ## - return tupla implicita
# def retorna_valores():
#     return 2, 4, 8

# print(retorna_valores())


## - Ejercicios #24 a #28
# 24
# Crear una función que reciba un número y una lista, e imprima {"Todos los valores son divisibles por {numero}"} si son todos divisibles, o {"Hay valores que no se pueden dividir por {numero}"} en caso contrario


# def todos_divisibles(lista, numero):
    
#     for i in lista:
#         if i % numero != 0:
#             return f'No son todos divisibles por {numero}'
#     return f'Son todos divisibles por {numero}'

# print(todos_divisibles([2,4,6,8,10,13], 2))

# # 26
# # Crear una función que reciba una tupla de palabras y retorne una frase uniendo esas palabras separadas por un espacio

# def crear_frase(palabras):
#     resultado = ""
#     for palabra in palabras:
#         resultado += palabra + " "
#     return resultado

# print(crear_frase(["Hola", "Mundo.", "Que", "disfruten", "su", "dia"]))

## - Argumentos por nombre vs por posición
# def saluda(nombre, apellido):
    
#     return f'Hola, me llamo {nombre} {apellido}'

# print(saluda("Mauricio", "Cuello"))
# print(saluda("Cuello", "Mauricio"))

# print(saluda(nombre="Mauricio", apellido="Cuello"))
# print(saluda(apellido="Cuello", nombre="Mauricio"))


## - Parametros por defecto
# def saluda(nombre, apellido=""):
    
#     return f'Hola, me llamo {nombre} {apellido}'

# print(saluda("Mauricio"))
# print(saluda("Mauricio", "Cuello"))
# print(saluda(nombre="Mauricio"))

# def resta(a=None, b=None):
    
#     if a and b:
#       return a - b
#     else:
#        return 'debe ingresar ambos datos'

# print(resta(5))


## - Pasaje de parametro por valor vs por referencia
mi_nombre = "mauricio"
mi_edad = 32
mis_familiares = ["Juan", "Abril", "Mariela", "Jesica", "Roberto"]

# def cambia_nombre(nombre: str):
#     nombre = nombre.capitalize()
#     print('local: ', nombre)

# cambia_nombre(mi_nombre)
# print('global:', mi_nombre)

# def cambia_familiar(lista: list):
    
#     lista.append("Hanna")
#     print('local:',lista)

# cambia_familiar(mis_familiares)
# print('global: ', mis_familiares)


## - r1 a r9 en examples.py
# import copy

# mi_lista = [[2, 8, -5, 24],[1, 3, 5, 7]]

# mi_numero = 5

# mi_lista2 = copy.deepcopy(mi_lista)
# mi_lista3 = mi_lista

# def cambia_valores(matriz):
#     for fila in matriz:
#         fila.append(0)

# cambia_valores(mi_lista3)

# print(mi_lista)
# print(mi_lista2)
# print(mi_lista3)

## - Argumentos indeterminados

# def suma(*args):
    
#     return sum(args)

# print(suma(5,10,40,20,3))

# def suma(**kwargs):
    
#     return sum(kwargs.values())

# print(suma(a=10, b=-5, c=8, d=-1))

# def resultado(nombre, *args, **kwargs):
    
#     print(f'Hola {nombre}! estas son tus notas')

#     for nota in args:
#         print(f'Nota: {nota}')

#     print(f'Le enviaremos una copia a {list(kwargs.values())}')


# resultado("Mauricio", 4, 8, 3, 9, 10, papa="Roberto", mama="Mariela")

## - Ejercicio #29

# TAREA

## - Recursividad

# def cuenta(numero):
#     numero -= 1

#     if numero > 0:
#         print(f'> {numero}')
#         cuenta(numero)
#     else:
#         print("Boom!!")

# cuenta(5)

def factorial(num):
    
    if num > 1:
        return num * factorial(num-1)
    else:
        return num

print(factorial(5))

## - Ejercicios #30 a #35
