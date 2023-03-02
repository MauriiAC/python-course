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
    
#     def establece_objetivo(self, meta):
#         self.meta = meta

#     def camina(self, pasos):
#         if pasos >= self.meta:
#             return f'Felicidades {self.nombre}, cumpliste tu objetivo'
#         else:
#             return 'No lograste tu objetivo, ponete las pilas!'


# messi = Persona("Lionel", "Messi", 35, None)
# cristiano = Persona("Cristiano", "Ronaldo", 38, None)
# riquelme = Persona("Roman", "Riquelme", 42, None)

# messi.establece_objetivo(500)
# cristiano.establece_objetivo(800)
# print(messi.camina(550))
# print(cristiano.camina(550))
# mauricio = Persona("Mauricio", "Cuello", 32, [messi, cristiano])

# print(Persona.saluda(messi))


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
# class Perro():
    
#     num_patas = 4
    
#     def __init__(self, nombre, raza, edad):
#         self.nombre = nombre
#         self.raza = raza
#         self.edad = edad
      
#     def __str__(self):
#         return f'{self.raza} de {self.edad} años'
      
#     def ladrar(self, cant):
#         return 'guau'*cant

# perro1 = Perro("cachito", "caniche", 2)
# perro2 = Perro("pepito", "dalmata", 4)

# print(perro1.ladrar(10))
# print(perro1.ladrar(2))

# print(Perro.num_patas)
# print(perro1.num_patas)

# print(perro1)
# print(perro2)


## - encapsulamiento, modificación controlada
## - relación entre clases

# class Persona():
    
#     def __init__(self, nom, ape, ed, perro=None):
#         self.nombre = nom
#         self.apellido = ape
#         self.__edad = ed
#         self.perro = perro

#     def saluda(self):
#         return f'Hola, me llamo {self.nombre} {self.apellido}'
    
#     def get_edad(self):
#         return f'Tengo {self.__edad} años'
    
#     def cumple_agno(self):
#         self.__edad += 1

#     def mi_perro(self):
#         if self.perro:
#             return f'Tengo un perro que se llama {self.perro.nombre}, que es un {self.perro.raza} de {self.perro.edad} años'
#         else:
#             return 'No tengo perro'

# messi = Persona("Lionel", "Messi", 35)

# print(dir(messi))
# print(messi._Persona__edad)

# class Perro():
    
#     num_patas = 4
    
#     def __init__(self, nombre, raza, edad):
#         self.nombre = nombre
#         self.raza = raza
#         self.edad = edad
      
#     def __str__(self):
#         return f'{self.raza} de {self.edad} años'
      
#     def ladrar(self, cant):
#         return 'guau'*cant

# perro1 = Perro("cachito", "caniche", 2)
# perro2 = Perro("pepito", "dalmata", 4)

# messi = Persona("Lionel", "Messi", 35, perro1)
# cristiano = Persona("Cristiano", "Ronaldo", 38)
# riquelme = Persona("Roman", "Riquelme", 42)

# print(messi.mi_perro())
# print(cristiano.mi_perro())

## - ejercicio de tickets
# 15-tickets.py

## - métodos especiales, dunder methods
# class Vector():

#     def __init__(self, data: list):
#         self.__data = data

#     def __str__(self):
#         return f'Los valores son: {self.__data}'
    
#     def __len__(self):
#         return len(self.__data)
    
#     def __getitem__(self, pos):
#         return self.__data[pos]

#     def __setitem__(self, pos, value):
#         self.__data[pos] = value

#     def get_pos(self, pos):
#         return self.__data[pos]

# v1 = Vector([1,2,3,5,7,8])
# v2 = Vector([1,2])
# # print(len(v1))
# # print(v1)
# print(v1[0])
# print(v1.get_pos(0))
# v1[1] = 20
# print(v1)

# for elem in v1:
#     print(elem)


## - herencia

class Persona():

    def __init__(self, nombre, apellido, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.apellido = apellido
        self.dni = dni

    def saluda(self):
        return f'Hola, me llamo {self.apellido} {self.nombre}'


class Empleado(Persona):

    def __init__(self, nombre, apellido, edad, dni, sueldo, horario):
        super().__init__(nombre, apellido, edad, dni)
        self.sueldo = sueldo
        self.horario = horario

    def saluda(self):
        return (
            f'{super().saluda()}'
            f' y gano {self.sueldo} euros'
        )
    
    def fichar(self, ingreso):
        if ingreso < self.horario:
            return f'Llegué {self.horario - ingreso} minutos temprano'
        else:
            return f'Llegué {ingreso - self.horario} minutos temprano'
        
class Seguridad(Empleado):

    def __init__(self, nombre, apellido, edad, dni, sueldo, horario, vehiculo, arma):
        super().__init__(nombre, apellido, edad, dni, sueldo, horario)
        self.vehiculo = vehiculo
        self.arma = arma
    
    def llamar_policia(self, mensaje):
        return f'Llamo a la policía y les digo que {mensaje}'     

persona1 = Persona("Mauricio", "Cuello", 32, 1351351)
empleado1 = Empleado("Cristiano", "Ronaldo", 38, 68074808, 1200, 360)
seguridad1 = Seguridad("Lionel", "Messi", 35, 15668406, 1100, 300, "Fiat 600", "AK-47")

# print(persona1.saluda())
# print(empleado1.saluda())
# print(seguridad1.saluda())

## - polimorfismo
# saludadores = [persona1, empleado1, seguridad1]

# for saludador in saludadores:
#     print(saludador.saluda())

# ## - duck typing

# class CosaQueSaluda():

#     def __init__(self, nombre) -> None:
#         self.nombre = nombre

#     def saluda(self):
#         return f'Hola, me llamo {self.nombre}'

# cosa1 = CosaQueSaluda("cosa")

# saludadores = [persona1, empleado1, seguridad1, cosa1]

# for saludador in saludadores:
#     print(saludador.saluda())


## - herencia multiple

# class Mamifero():

#     def __init__(self, cant_mamas, esp_vida):
#         self.cant_mamas = cant_mamas
#         self.esp_vida = esp_vida
#         self.peso = 0.5
    
#     def mamar(self, tiempo):
#         self.peso += tiempo * 0.5


# class AnimalMarino():

#     def __init__(self, tiene_branqueas, especie):
#         self.tiene_branqueas = tiene_branqueas
#         self.especie = especie

#     def nadar(self):
#         return 'Estoy nadando...'
    
# class Cetaceo(Mamifero, AnimalMarino):

#     def __init__(self, cant_mamas, esp_vida, tiene_branqueas, especie, caracteristicas):
#         Mamifero.__init__(self, cant_mamas, esp_vida)
#         AnimalMarino.__init__(self, tiene_branqueas, especie)
#         self.caracteristicas = caracteristicas


# cetaceo1 = Cetaceo(4, 40, True, "Ballena", "Nada muy profundo")

# print(cetaceo1.nadar())
# print(cetaceo1.peso)
# cetaceo1.mamar(2)
# print(cetaceo1.peso)


## - https://games.washingtonpost.com/games/blackjack
# 'spades': '♠', 
# 'diamonds': '♦',
# 'clubs': '♣',
# 'hearts': '♥'

## - Para la clase que viene: instalar Eclipse y Java

