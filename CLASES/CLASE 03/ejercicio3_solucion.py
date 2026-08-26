"""
EJERCICIO 3 · INTEGRADOR — Un mismo sistema, los tres conceptos
Consigna: diseñar un sistema de figuras geométricas que combine:
  - Abstracción: decidir que lo único que nos importa de "una figura" es
    que sepa calcular su área (no nos importa el color, el material, etc).
  - Herencia: una clase base FiguraGeometrica y subclases concretas.
  - Polimorfismo: cada subclase sobreescribe area() a su manera, y el
    código que recorre la lista llama a .area() sin preguntar de qué
    clase es cada figura.
"""

import math


# Clase base: define el "contrato" común (abstracción). No sabe calcular
# un área real porque una "figura geométrica" en general no alcanza para
# eso — por eso lanza un error si alguien la usa directamente sin
# sobreescribir area() en una subclase.
class FiguraGeometrica:
    def area(self):
        raise NotImplementedError("Cada figura debe implementar su propio cálculo de área")


class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2


class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2


# Guardamos figuras de distintas clases en una misma lista: esto es
# posible porque todas heredan de FiguraGeometrica.
figuras = [
    Circulo(radio=3),
    Rectangulo(base=4, altura=5),
    Triangulo(base=6, altura=2),
]

# Polimorfismo: llamamos a .area() en cada una sin importar de qué clase
# es. Python decide en tiempo de ejecución qué versión de area() usar
# según el objeto real, no según el tipo declarado.
for figura in figuras:
    nombre_clase = type(figura).__name__
    print(f"{nombre_clase}: área = {figura.area():.2f}")
