## - Sintaxis
# datos_1 = ["Mauricio", "Cuello", 32, True, ["Barcelona", "Madrid", "Buenos Aires"]]
# datos_2 = ("Mauricio", "Cuello", 32, True, ["Barcelona", "Madrid", "Buenos Aires"])

## - Heteregoneas
# datos_2 = ("Mauricio", "Cuello", 32, True, ["Barcelona", "Madrid", "Buenos Aires"])

# ## - Inmutabilidad
# datos_1 = ["Mauricio", "Cuello", 32, True, ["Barcelona", "Madrid", "Buenos Aires"]]
# datos_2 = ("Mauricio", "Cuello", 32, True, ["Barcelona", "Madrid", "Buenos Aires"])

# datos_1[0] = "Lionel"
# print(datos_1)

# datos_2 = ("Lionel", "Cuello", 32, True, ["Barcelona", "Madrid", "Buenos Aires"])
# print(datos_2)

## - Tupla de un solo elemento
# datos = ["Mauricio"]
# print(datos)
# datos = ("Mauricio",)
# print(datos[0])


## - Indices
# datos_2 = ("Lionel", "Cuello", 32, True, ["Barcelona", "Madrid", "Buenos Aires"])
# print(datos_2[2])
# datos_2 = ("Lionel", "Cuello", 32, True, ["Barcelona", "Madrid", "Buenos Aires"])
# datos_2[-1][0] = "Sevilla"
# print(datos_2)

## - Slicing
# print(datos_2[2:4])

# datos_2[2:4] = ("Lionel", "Messi") # ERROR!
# print(datos_2)

## - Concatenación
# datos1 = ("Mauricio", "Lionel", "Cristiano", "Lionel")
# datos2 = ("Mariana", "Juan")

# print(datos2 + datos1)

## - Anidamiento
# datos_2 = ("Lionel", "Cuello", 32, True, ("Barcelona", "Madrid", "Buenos Aires"))

# ## - Funciones integradas
# datos_2 = ("Lionel", "Cuello", 32, True, ("Barcelona", "Madrid", "Buenos Aires"))
# # print(len(datos_2))

# print(datos_2.count(32))
# print(datos_2.index(True))


# ## - Parseo con listas
# datos1 = ("Mauricio", "Lionel", "Cristiano", "Lionel")
# datos2 = list(datos1)
# datos2.append("Juana")
# datos1 = tuple(datos2)

# print(datos1)


