import math as m
class Circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return (m.pi * (self.radio**2))
    def peritro(self):
        return (m.pi*2*self.radio)

circulo1 = Circulo(23)
Area = circulo1.area()
Perimetro = circulo1.peritro()
print (Area)
print (Perimetro)

class Rectangulo:
    def __init__(self, alto, ancho):
        self.alto = alto
        self.ancho = ancho
    
    def área(self):
        return self.alto * self.ancho
    def perímetro(self):
        return ((self.alto * 2) + (self.ancho * 2))

rectangulo1 = Rectangulo(12, 24)
print ("el área del reactangulo es: ", rectangulo1.área())
print ("el perímetro del rectangulo es: ", rectangulo1.perímetro())

class Libro:
    def __init__(self, titulo, autor, ndp):
        self.titulo = titulo
        self.autor = autor
        self.ndp = ndp
    
    def información(self):
        print ("Titulo: ", self.titulo)
        print ("Autor: ", self.autor)
        print ("Número de páginas: ", self.ndp)

libro1 = Libro("Invisible", "Eloy Moreno", "200")
print ("informaión de libro 1: ")
libro1.información()