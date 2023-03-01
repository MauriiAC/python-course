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
class Persona():
    
    def __init__(self, nom, ape, ed):
        self.nombre = nom
        self.apellido = ape
        self.edad = ed
    
    def saluda(self):
        return f'Hola, me llamo {self.nombre} {self.apellido}'

messi = Persona("Lionel", "Messi", 35)
cristiano = Persona("Cristiano", "Ronaldo", 38)
riquelme = Persona("Roman", "Riquelme", 42)

# print(messi.nombre)
# print(messi.edad)
# print(cristiano.apellido)

print(messi.saluda())
print(cristiano.saluda())

## - métodos de instancia


## - atributo de clase vs atributo de instancia


## - encapsulamiento, modificación controlada


## - relación entre clases


## - 

