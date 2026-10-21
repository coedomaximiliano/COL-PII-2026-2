#Figuras geométricas encapsuladas
#Definí una clase base Figura con un atributo privado __color (encapsulamiento) recibido por constructor, y un destructor __del__ que imprima un mensaje al eliminarse la figura.
#Agregale un método area() que lance NotImplementedError, para que cada subclase lo implemente a su manera.
#Definí las subclases Circulo, Rectangulo y Triangulo, cada una con sus propios atributos y su propia implementación de area() (herencia simple + polimorfismo).
#Exponé el color de solo lectura con @property, sin permitir modificarlo desde afuera de la clase.
#Tu programa debe:
#Crear al menos una figura de cada subclase, con colores distintos.
#Recorrer una lista con las tres figuras y mostrar el área de cada una llamando siempre al mismo método area() (polimorfismo).
#Mostrar el color de cada figura usando la property, sin acceder directamente al atributo privado.


class Figura:
    def __init__(self, color):
        self.__color = color

    @property
    def color(self):
        return self.__color

    def area(self):
        raise NotImplementedError("El método area() debe ser implementado por las subclases.")

    def __del__(self):
        print(f"Figura de color {self.__color} eliminada.")

class Circulo(Figura):
    def __init__(self, color, radio):
        super().__init__(color)
        self.radio = radio

    def area(self):
        import math
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
        return 0.5 * self.base * self.altura

circulo = Circulo("rojo", 5)
rectangulo = Rectangulo("azul", 10, 4)
triangulo = Triangulo("verde", 8, 6)

# Lista de figuras
figuras = [circulo, rectangulo, triangulo]

# Polimorfismo: se llama al mismo método area()
# independientemente del tipo de figura
for figura in figuras:
    print(f"Figura: {type(figura).__name__}")
    print(f"Color: {figura.color}")
    print(f"Área: {figura.area():.2f}")
    print("-" * 30)