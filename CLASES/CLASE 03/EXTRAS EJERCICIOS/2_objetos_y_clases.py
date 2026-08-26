"""
EJERCICIOS — OBJETOS Y CLASES
Recordá: una clase es un molde que define atributos y métodos. Un objeto
es una instancia concreta de esa clase, con sus propios valores.
"""

# ============================================================
# Ejercicio 1 (Fácil)
# Definí una clase Libro con atributos titulo, autor y paginas. Agregále
# un método resumen() que imprima esos datos en un mensaje.
# ============================================================


class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def resumen(self):
        print(f'"{self.titulo}" de {self.autor} ({self.paginas} páginas)')


libro1 = Libro("Ficciones", "Jorge Luis Borges", 203)
libro1.resumen()


# ============================================================
# Ejercicio 2 (Medio)
# Definí una clase Circulo con atributo radio, y métodos area() y
# perimetro(). Creá una LISTA de varios círculos distintos y calculá la
# suma de todas sus áreas.
# ============================================================

import math


class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio


circulos = [Circulo(2), Circulo(3.5), Circulo(1)]
area_total = sum(c.area() for c in circulos)
print(f"Área total de {len(circulos)} círculos: {area_total:.2f}")


# ============================================================
# Ejercicio 3 (Difícil)
# Definí una clase Estudiante con atributo nombre y una lista de notas
# (vacía al crear el objeto). Agregále un método agregar_nota(nota), un
# método promedio() y un método aprobado() que devuelva True si el
# promedio es mayor o igual a 6.
# ============================================================


class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def promedio(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)

    def aprobado(self):
        return self.promedio() >= 6


est = Estudiante("Martín")
for nota in [7, 5, 8, 6]:
    est.agregar_nota(nota)

print(f"{est.nombre} — promedio: {est.promedio():.1f} — aprobado: {est.aprobado()}")
