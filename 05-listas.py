## - Sintaxis
# nombres = ["Mauricio", "Ana", "Juan", "Maria"]
# print(nombres)

# ## - Heteregoneas
# datos = ["Mauricio", "Cuello", 32, True]
# print(datos)

# ## - Indices
# datos = ["Mauricio", "Cuello", 32, True]
# print(datos[0])
# print(datos[0][0])
# print(datos[-1])

# ## - Concatenación
# datos = ["Mauricio", "Cuello", 32, True]
# datos2 = ["Ana", "Acuña", 40, False]

# print(datos + datos2)

## - Anidamiento
# datos = ["Mauricio", "Cuello", "32", True, ["Barcelona", "Madrid", "Buenos Aires"]]

# print(datos[-1][0][-1])
# print(datos[2][0])

## - Mutabilidad
# mi_string = "mauricio"
# mi_string[0] = "M"

# mi_lista = ["mauricio", "lionel", "cristiano"]
# mi_lista[0][0] = "M"

# datos = ["Mauricio", "Cuello", "32", True, ["Barcelona", "Madrid", "Buenos Aires"]]
# datos[-1][0] = "Sevilla"

# print(datos)

## - Slicing, asignación por slicing
datos = ["Mauricio", "Cuello", "32", True, ["Barcelona", "Madrid", "Buenos Aires"]]
# print(datos[::-1])
# datos[1:3] = ["Ana", 55, "ana@gmail.com"]
# print(datos)
# datos[1:3] = []
# print(datos)

## - Funciones integradas
# datos = ["Mauricio", "Cuello", "32", True, ["Barcelona", "Madrid", "Buenos Aires"]]
# mi_lista = ["Mauricio", "Lionel", "Cristiano", "Lionel"]
# mi_lista.append("Soledad")
# mi_lista.append("Soledad " + "Pastouruti")

# print(len(mi_lista))
# mi_lista.pop(1)
# print(mi_lista)

# print(mi_lista.count("Lionel"))
# print(mi_lista.index("Lionel"))


## - Ejercicios #6 al #7
# Dada la lista [5, 7, 3, 0, 4, 0, 4, 3, 4, 8, 6, 9, 8, 5, 1, 2, 3, 9, 7, 2, 1, 6] pedir al usuario que ingrese un número entre 0 y 9 y devolver:
# - cuantas veces aparece el número en la lista
# - el indice de la segunda vez que aparece en la lista (suponer q aparece dos veces)

# mi_lista = [5, 7, 3, 0, 4, 0, 4, 3, 4, 8, 6, 9, 8, 5, 1, 2, 3, 9, 7, 2, 1, 6]

# num = int(input("Ingrese el numero q quiere buscar: "))

# # print(mi_lista.index(num))

# long_sublista = mi_lista.index(num) + 1

# mi_lista = mi_lista[mi_lista.index(num)+1:]

# # print(mi_lista)
# print(mi_lista.index(num) + long_sublista)

