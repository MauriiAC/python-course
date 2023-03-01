## - Fundamento de la POO
  # Bloques de código excesivamente grandes
  # Modularización
  # Código difícil de interpretar (cod spaguetti)
  # Difícil de depurar y escalar
  # Difícil la reutilización
  # Los errores posiblemente provocaban el crush de la aplicación
  # Complejo el control de la interacción con usuarios
  # Encapsulamiento

## - Como se piensa con POO? id, caract, funcionalidades


## - Diagrama de clase
# http://diagramaweb.com/wp-content/uploads/2020/08/diagrama-de-clases-tipos-1024x606.png


## - partes importantes: clase, objetos, metodo constructor, self, atributos de instancia


## - primer ejemplo
# class Persona():
    
#     def __init__(self, nom, ape, ed, ami):
#         self.nombre = nom
#         self.apellido = ape
#         self.edad = ed
#         self.amigos = ami
    
#     def add_amigo(self, amigo):
#         self.amigos.append(amigo)

#     def listar_amigos(self):
#         mis_amigos = []
#         for persona in self.amigos:
#             mis_amigos.append(persona.nombre)
#         lista_nombres = ', '.join(mis_amigos)
#         return f'Soy amigo de {lista_nombres}'

#     def saluda(self):
#         return f'Hola, me llamo {self.nombre} {self.apellido}'
    
# messi = Persona("Lionel", "Messi", 35, None)
# cristiano = Persona("Cristiano", "Ronaldo", 38, None)
# riquelme = Persona("Roman", "Riquelme", 42, None)

# print(Persona.saluda(messi))

# mauricio = Persona("Mauricio", "Cuello", 32, [messi, cristiano])

# print(riquelme.listar_amigos())

# # print(messi.nombre)
# # print(messi.edad)
# # print(cristiano.apellido)

# # print(messi.saluda())
# # print(cristiano.saluda())
# print(mauricio.listar_amigos())
# mauricio.add_amigo(riquelme)
# print(mauricio.listar_amigos())


## - métodos de instancia
#     def saluda(self):
#         return f'Hola, me llamo {self.nombre} {self.apellido}'

## - atributo de clase vs atributo de instancia, metodos con parametros
class Perro():
    
    num_patas = 4
    
    def __init__(self, nombre, raza, edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
      
    def __str__(self):
        return f'{self.raza} de {self.edad} años'
      
    def ladrar(self, cant):
        return 'guau'*cant

perro1 = Perro("cachito", "caniche", 2)
perro2 = Perro("pepito", "dalmata", 4)
# print(perro1.ladrar(10))
# print(perro1.ladrar(2))

# print(Perro.num_patas)
# print(perro1.num_patas)

print(perro1)
print(perro2)

## - encapsulamiento, modificación controlada


## - relación entre clases


## - herencia


## - polimorfismo

