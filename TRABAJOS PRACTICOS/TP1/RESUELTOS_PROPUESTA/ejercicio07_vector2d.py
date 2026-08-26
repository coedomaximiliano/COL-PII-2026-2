"""
EJERCICIO 7 (Difícil) — Métodos especiales (dunder): Vector2D
Consigna: clase Vector2D con x e y. Implementar __add__, __sub__, __eq__ y
__str__ para poder sumar y restar vectores con + y -, compararlos con == y
mostrarlos con print() de forma legible.
"""


class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, otro):
        return Vector2D(self.x + otro.x, self.y + otro.y)

    def __sub__(self, otro):
        return Vector2D(self.x - otro.x, self.y - otro.y)

    def __eq__(self, otro):
        return self.x == otro.x and self.y == otro.y

    def __str__(self):
        return f"({self.x}, {self.y})"


v1 = Vector2D(2, 3)
v2 = Vector2D(1, 5)

print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v1 + v2 = {v1 + v2}")
print(f"v1 - v2 = {v1 - v2}")
print(f"v1 == v2: {v1 == v2}")
print(f"v1 == Vector2D(2, 3): {v1 == Vector2D(2, 3)}")
