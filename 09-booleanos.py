## - Sintaxis
# True
# False

# ## - Equivalencia numerica
# lista = [1, 2, 5, True, "Hola", [True, 1], "Hola"]

# print(lista.count(True))

## - Operadores relacionales
# print(1 == True)

## - Operadores lógicos, not, and, or
# print(1 == True and "hola" != "Hola")
# print( (not 5 > 2) or (2 == 5) or "Hola" == "hola".capitalize() )

## - Precedencia
# print(not False or False and False or True)
# """
# not False or False and False or True
# True or False and False or True
# True or False or True
# """

# ## - Ejemplo
# tengo_dinero = True
# esta_lloviendo = True
# tengo_paraguas = True

# print(tengo_dinero and (not esta_lloviendo or tengo_paraguas))

## - Cortocircuito lógico, autocasting, weird cases

# print(("True" and "False") == (True and False))
# print("False" == False)

# True and print("Hola")
# False and print("Chau")

# print(bool([False, False]))

# print("True" and "False")
# print(True and False)

# True or print("hola")
# False or print("hola") or 125 or print("chau")