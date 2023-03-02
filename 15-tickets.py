class Cliente():
    
    def __init__(self, nombre, apellido, edad, dni):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.__dni = dni

    def comprar_ticket(self, evento):
        self.__ticket = evento.generar_ticket(self.__dni)
        if self.__ticket:
            print(f'Su nro de ticket es {self.__ticket}')
        else:
            print('Ya no hay ticket disponibles')
    
    def ingresar_evento(self, evento):
        if not self.__ticket:
            print('No posee ticket para el evento')
            return
        ingreso = self.__ticket.corroborar_ticket(self.__dni)
        if ingreso:
            print(evento.bienvenida())
        else:
            print(evento.rechazo())

class Evento():
    
    def __init__(self, numero, titulo, fecha, cupo):
        self.__numero = numero
        self.__titulo = titulo
        self.__fecha = fecha
        self.__cupo = cupo
        self.__siguiente_ticket = 1

    def generar_ticket(self, dni):
        if self.__siguiente_ticket > self.__cupo:
            return None
        else:
            nuevo_ticket = Ticket(self.__siguiente_ticket, dni)
            self.__siguiente_ticket += 1
            return nuevo_ticket
        
    def bienvenida(self):
        return f'Bienvenid@ a {self.__titulo}'
    
    def rechazo(self):
        return f'Usted no posee un ticket valido'

class Ticket():

    def __init__(self, numero, dni):
        self.__numero = numero
        self.__dni = dni
        self.__estado = "sin usar"
  
    def __str__(self):
        return str(self.__numero)

    def corroborar_ticket(self, dni):
        
        if self.__estado == "sin usar" and dni == self.__dni:
            self.__estado = "usado"
            return True
        else:
            return False

evento1 = Evento(1, "Recital de Chayanne", "2023-05-01", 5)

cliente1 = Cliente("Juana", "Garcia", 50, 123456)
cliente2 = Cliente("Juan", "Garcia", 22, 321654)
cliente3 = Cliente("Gabriela", "Garcia", 31, 459879)
cliente4 = Cliente("Mariano", "Garcia", 15, 7987987)
cliente5 = Cliente("Mauricio", "Garcia", 28, 987987)
cliente6 = Cliente("Marcelo", "Garcia", 30, 1781899)

cliente1.comprar_ticket(evento1)
cliente2.comprar_ticket(evento1)
cliente3.comprar_ticket(evento1)
cliente4.comprar_ticket(evento1)
cliente5.comprar_ticket(evento1)
cliente6.comprar_ticket(evento1)

cliente1.ingresar_evento(evento1)
cliente1.ingresar_evento(evento1)
cliente2.ingresar_evento(evento1)
cliente3.ingresar_evento(evento1)
cliente4.ingresar_evento(evento1)
cliente5.ingresar_evento(evento1)
cliente6.ingresar_evento(evento1)


