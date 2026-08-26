"""
EJERCICIO 2 (Fácil) — Clase Rectangulo
Consigna: definir una clase Rectangulo con atributos base y altura, y dos
métodos: area() y perimetro().
"""


class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)


r1 = Rectangulo(4, 6)
print(f"Área: {r1.area()}")
print(f"Perímetro: {r1.perimetro()}")
