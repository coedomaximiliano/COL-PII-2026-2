#Ejercicio 1: Figuras Geométricas Encapsuladas

import math
from turtle import color


#Clase base para todas las figuras geométricas
class figura:
    def __init__ (self, nombre, color):
        self.nombre = nombre
        self.__color = color

#Property para obtener el color de la figura sin acceder al atributo privado (__color)
    @property
    def color(self):
        return self.__color

#Metodo que implementa cada subclase (area)
    def area(self):
        raise NotImplementedError("El método area() debe ser implementado por cada subclase")

#Destructor que se ejecuta para eliminar cada referencia de clase
    def __del__(self):
        print(f"Se ha eliminado la figura {self.nombre} de color {self.__color}")




#Subclase Circulo
class Circulo(figura):
    def __init__(self, radio, color):
       # LLamamos al constructor de la clase Figura
       super().__init__("Círculo", color)
       self.radio = radio  #Atributo propio de la clase Circulo
           


    # Implementacion propia del metodo area()
    def area(self):
        return math.pi * self.radio ** 2

    

#Subclase Rectangulo
class Rectangulo(figura):
    def __init__(self, color, base, altura):
        super().__init__("Rectángulo", color)

        #Atributos propios de la clase Rectangulo
        self.base = base    
        self.altura = altura
    # Implementacion propia del metodo area()
    def area(self):
        return self.base * self.altura
    


#Subclase Triangulo
class Triangulo(figura):
    def __init__(self, color, base, altura):
        super().__init__("Triángulo", color)

        #Atributos propios de la clase Triangulo
        self.base = base
        self.altura = altura

    # Implementacion propia del metodo area()
    def area(self):
        return (self.base * self.altura) / 2

#Creo una figura de cada tipo con colores y tamaños distintos
circulo1 = Circulo(5, "Rojo")
rectangulo1 = Rectangulo("Azul", 4, 6)
triangulo1 = Triangulo("Verde", 3, 4)

#Guardo todas las figuras en una lista
figuras = [circulo1, rectangulo1, triangulo1]

#Itero sobre la lista de figuras y muestro su nombre, color y area
for figura in figuras:
    print(f"Figura: {type(figura).__name__}")
    print(f"Color: {figura.color}")
    print(f"Área: {figura.area():.2f}")
    print("-----------------------------")

      