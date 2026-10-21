import math


class Figura:
    def __init__(self, color):
        self.__color = color

    @property
    def color(self):
        return self.__color

    def area(self):
        raise NotImplementedError("Cada figura debe calcular su área.")

    def __del__(self):
        print(f"Se eliminó la figura de color {self.__color}.")


class Circulo(Figura):
    def __init__(self, color, radio):
        super().__init__(color)
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2


class Rectangulo(Figura):
    def __init__(self, color, ancho, alto):
        super().__init__(color)
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto


class Triangulo(Figura):
    def __init__(self, color, base, altura):
        super().__init__(color)
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2


figura_circular = Circulo("amarillo", 4)
figura_rectangular = Rectangulo("violeta", 6, 3)
figura_triangular = Triangulo("naranja", 5, 8)

lista_figuras = [
    figura_circular,
    figura_rectangular,
    figura_triangular
]

for elemento in lista_figuras:
    print(f"Tipo: {type(elemento).__name__}")
    print(f"Color: {elemento.color}")
    print(f"Área: {elemento.area():.2f}")
    print()