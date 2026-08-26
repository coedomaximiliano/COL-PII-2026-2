"""
EJERCICIO 1 (Fácil) — Clase Punto
Consigna: definir una clase Punto con atributos x e y, y un método
distancia_al_origen() que devuelva la distancia euclídea al punto (0, 0).
"""

import math


class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia_al_origen(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)


p1 = Punto(3, 4)
p2 = Punto(0, 7)

print(f"Distancia de p1 al origen: {p1.distancia_al_origen()}")
print(f"Distancia de p2 al origen: {p2.distancia_al_origen()}")
