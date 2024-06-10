class Cuenta_Bancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo 

    def retirar(self, monto):
        self.saldo -= monto
        if monto > self.saldo:
            print("no tiene saldo suficiente")
        print ("Ha retirado ", monto)
    
    def depositar(self, monto):
        self.saldo += monto
        print("Ha depositado ", monto)

    def mostrar_saldo(self):
        print("tu saldo actual es: ", self.saldo)
    
cuenta1 = Cuenta_Bancaria("Jairo", 2000)
print("el titular de la cuenta es: ", cuenta1.titular)
cuenta1.retirar(300)
cuenta1.mostrar_saldo()
cuenta1.depositar(8000)
cuenta1.mostrar_saldo()

class Estudiante:
    def __init__(self, nombre, edad, notas):
        self.nombre = nombre
        self.edad = edad
        self.notas = notas
    
    def agregar_nota(self, nota):
        self.notas.append(nota)
        print ("las notas del estudiante son: ", self.notas)

    def promedio(self):
        suma = sum(self.notas)
        prom = suma/(len(self.notas))
        print ("Promedio de notas: ", prom)

    def información(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)
        self.promedio()

estudiante1 = Estudiante("Pepe", 23, [8, 12, 15, 13])
estudiante1.información()
estudiante1.agregar_nota(17)
print (estudiante1.nombre)

class Agenda:
    def __init__(self):
        self.contactos = {}
    
    def agregar_contacto(self, nombre, telefono):
        self.contactos[nombre] = telefono
        print ("Agregaste a ", nombre, "a tus contactos")

    def eliminar_contacto(self, nombre):
        if nombre not in self.contactos:
            print ("No se encontró a", nombre, "en tus contactos.")
        else:
            del self.contactos[nombre]
            print ("Eliminaste a ", nombre, "de tus contactos")
        
    
    def mostrar_contactos(self):
        print("Tus contactos son: ", self.contactos)
    
mi_agenda = Agenda()
mi_agenda.agregar_contacto("Enrrique", 987678654)
mi_agenda.agregar_contacto("María", 934975876)
mi_agenda.agregar_contacto("Danilo", 945988102)
mi_agenda.mostrar_contactos()
mi_agenda.eliminar_contacto("María")
mi_agenda.mostrar_contactos()
mi_agenda.eliminar_contacto("Cristel")
    
