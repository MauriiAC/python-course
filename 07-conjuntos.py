## - Definicion: una colección no ordenada de elementos únicos

## - Sintaxis
# mi_lista = ["Mauricio", "Lionel", "Cristiano", "Lionel"]
# mi_tupla = ("Mauricio", "Lionel", "Cristiano", "Lionel")
# mi_conjunto = {"Mauricio", "Lionel", "Cristiano", "Lionel"}

# print(type(mi_conjunto))

## - Set vacío
# mi_tupla = ()
# print(type(mi_tupla))
# mi_conjunto = set()
# print(type(mi_conjunto))

# ## - Heterogeneos, tipos permitidos
# mi_lista = ["Mauricio", "Lionel", "Cristiano", 30, True, ("Barcelona", "Madrid", "Sevilla")]
# mi_tupla = ("Mauricio", "Lionel", "Cristiano", 30, True, ("Barcelona", "Madrid", "Sevilla"))
# mi_conjunto = {"Mauricio", "Lionel", "Cristiano", 30, True, ("Barcelona", "Madrid", "Sevilla")}

# print(mi_lista)
# print(mi_tupla)
# print(mi_conjunto)

## - Parseo con otras colecciones
# mi_lista = ["Mauricio", "Lionel", "Cristiano", 30, True, 30]
# mi_tupla = ("Mauricio", "Lionel", "Cristiano", 30, True, 30)
# mi_conjunto = {"Mauricio", "Lionel", "Cristiano", 30, True, 30}

# print(mi_lista)
# print(mi_tupla)
# print(mi_conjunto)

# print(set('pepe'))
# {"pepe"}

## - Funciones integradas

# mi_conjunto = {"Mauricio", "Lionel", "Cristiano", 30, True}

# print(mi_conjunto[1:3]) ERROR!
# mi_conjunto.add("Juana")
# mi_conjunto.add("Mauricio")
# mi_conjunto.update({"Juana", "Maria", "Pepe", "Lionel"})

# mi_conjunto.pop()
# mi_conjunto.pop()

# print(mi_conjunto)
