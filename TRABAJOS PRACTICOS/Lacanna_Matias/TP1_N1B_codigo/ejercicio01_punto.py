# Ejercicio 1 
import math


class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia_al_origen(self):
        return math.hypot(self.x, self.y)  


if __name__ == "__main__":
    p1 = Punto(3, 4)
    p2 = Punto(-2, 7)
    print(f"Distancia de ({p1.x}, {p1.y}) al origen: {p1.distancia_al_origen():.2f}")
    print(f"Distancia de ({p2.x}, {p2.y}) al origen: {p2.distancia_al_origen():.2f}")
