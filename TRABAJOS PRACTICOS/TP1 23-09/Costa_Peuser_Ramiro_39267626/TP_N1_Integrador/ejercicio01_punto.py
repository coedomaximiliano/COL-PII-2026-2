
# Definí una clase Punto con atributos x e y.
#Agregále un método distancia_al_origen() que devuelva la distancia entre el punto y el origen (0, 0).
# Tu programa debe:
# Crear al menos dos puntos distintos.
# Mostrar por consola la distancia al origen de cada uno.


import math


class Punto:
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def distancia_al_origen(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

# Crear al menos dos puntos distintos
punto1 = Punto(3, 4)
punto2 = Punto(1, 7)

# Mostrar por consola la distancia al origen de cada uno
print(f"Distancia del punto 1 al origen: {punto1.distancia_al_origen()}")
print(f"Distancia del punto 2 al origen: {punto2.distancia_al_origen()}")