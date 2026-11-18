# Ejercicio 1 
import math


class Figura:
    def __init__(self, color):
       
        self.__color = color

    def __del__(self):
       
        print(f"Se eliminó la figura {self.__class__.__name__} de color {self.__color}")

    @property
    def color(self):
      
        return self.__color

    def area(self):
        
        raise NotImplementedError("Cada subclase debe implementar area()")


class Circulo(Figura):
    def __init__(self, color, radio):
        super().__init__(color)
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2


class Rectangulo(Figura):
    def __init__(self, color, base, altura):
        super().__init__(color)
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


class Triangulo(Figura):
    def __init__(self, color, base, altura):
        super().__init__(color)
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura / 2


if __name__ == "__main__":
    figuras = [
        Circulo("rojo", 3),
        Rectangulo("azul", 4, 5),
        Triangulo("verde", 6, 2),
    ]

   
    for f in figuras:
        print(f"{f.__class__.__name__} | color: {f.color} | área: {f.area():.2f}")

    
    try:
        figuras[0].color = "negro"
    except AttributeError:
        print("No se puede modificar el color: es de solo lectura")

   
    del f
    del figuras
    print("Fin del programa")
