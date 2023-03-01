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

# def factorial(num):
    
#     if num > 1:
#         return num * factorial(num-1)
#     else:
#         return num

# print(factorial(5))

## - Ejercicios #30 a #35
# 30
# Crear una función que reciba dos string y devuelva la posición donde se encuentra el segundo string dentro del primero
# en caso que no se encuentre, devolver -1
# NO ESTÁ PERMITIDO usar funciones de búsqueda como find o rfind
# Ej "Hello, welcome to my world.", "welcome" --> 7

# def pos_substr(main, sub):

#     for posM, charM in enumerate(main):
#         if ( main[posM:posM+len(sub)] == sub):
#             return posM
#     return -1

# print(pos_substr("Hello, welcome to my world.", "white"))

# 31
# Crear una función que reciba una lista ordenado de números enteros y un número objetivo
# la función debe devolver True si existe una combinación de dos números de la lista que 
# sumados arrojen como resultado el número objetivo
# Ej. [1,5,9,11,15], 10 --> True
# Ej. [1,5,9,11,15], 11 --> False


# def matchSuma(arr, target):

    # for i, num_i in enumerate(arr):
    #     for j, num_j in enumerate(arr[i+1:]):
    #         if num_i + num_j == target:
    #             return True
    # return False


    # start = 0
    # end = len(arr) - 1

    # while(start < end):
    #     sum = arr[start] + arr[end]

    #     if sum == target:
    #         return True
    #     elif sum < target:
    #         start += 1
    #     else:
    #         end -= 1
    # return False

# print(matchSuma([1,5,9,11,15], 10))
# print(matchSuma([1,5,9,11,15], 11))

# 32
# Crear una función que reciba una lista con los valores de cotización de una acción en el tiempo
# la función debe devolver el máximo beneficio de haber comprado y vendido dicha acción
# Ej. acciones: [4, 3, 2, 5, 11] --> mayor ganancia: 9

# def maxRevenue(values):

#     max = values[1] - values[0]

#     for i, val_i in enumerate(values):

#         for j, val_j in enumerate(values[i+1:]):

#             possibleRevenue = val_j - val_i
#             if possibleRevenue > max:
#                 max = possibleRevenue
#     return max

# print(maxRevenue([4, 3, 2, 5, 11]))

# 33
# Crear una función que reciba una lista que puede contener listas o números como elementos
# La función debe devolver la suma de todos los números de todas las sublistas
# Ej. [1,2,3,4] --> 10
# Ej. [ [2,4] , [1], [4,2,1] ] --> 14
# Ej. [ 2, [3,4], 5, [-3, [6 , [ 4,5 ] ] ] ] --> 26


# def sumar_lista(lista,contador):
#     for i in lista:
#         if type(i)==int:
#             contador += i
#         else:
#             contador=sumar_lista(i,contador)
#     return contador

# lista1 = [1,2,3,4] 
# lista2 = [ [2,4] , [1], [4,2,1] ]
# lista3 = [ 2, [3,4], 5, [-3, [6 , [ 4,5 ] ] ] ]
# print(f"sumar {lista1} = {sumar_lista(lista1,0)}")
# print(f"sumar {lista2} = {sumar_lista(lista2,0)}")
# print(f"sumar {lista3} = {sumar_lista(lista3,0)}")

# 35
# Crear un bracket validator. La idea es que chequee que los brackets estén balanceados correctamente.
# Los brackets válidos son los siguientes: [ ] ( ) { }
# Ej. input: "{[]()}" --> True
#     input: "{[(])}" --> False
#     input: "{[([{()[]{}}])]}" --> True


# def bracket_validator(input_str: str):
#     open_brackets = ["[", "{", "("]
#     close_brackets = ["]", "}", ")"]
#     brackets = []
#     for char in input_str:
#         if char in open_brackets:
#             brackets.append(char)
#         elif char in close_brackets:
#             open_bracket = brackets.pop()
#             if (char == "]" and open_bracket != "[") \
#                     or (char == "}" and open_bracket != "{") \
#                     or (char == ")" and open_bracket != "("):
#                 return False

#     if len(brackets) == 0:
#         return True
#     else:
#         return False

# s1 = "{[]()}"
# s2 = "{[(])}"
# s3 = "{[([{()[]{}}])]}"
# print(bracket_validator(s1))
# print(bracket_validator(s2))
# print(bracket_validator(s3))


# import time

# my_list = list(range(1000000))
# my_set = set(my_list)

# start_time_list = time.time()
# if 999999 in my_list:
#     print('Found it')
# else:
#     print('Not found it')

# end_time_list = time.time()
# time_in_list = end_time_list-start_time_list
# print('time searching in list: ', time_in_list)

# start_time_set = time.time()
# if 999999 in my_set:
#     print('Found it')
# else:
#     print('Not found it')

# end_time_set = time.time()
# time_in_set = end_time_set-start_time_set
# print('time searching in set: ', time_in_set)


# print('ratio: ', time_in_list/time_in_set)