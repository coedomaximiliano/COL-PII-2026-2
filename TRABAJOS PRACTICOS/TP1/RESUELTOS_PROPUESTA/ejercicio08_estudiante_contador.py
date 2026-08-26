"""
EJERCICIO 8 (Difícil) — Atributos y métodos de clase: Estudiante
Consigna: clase Estudiante con atributo de instancia nombre, y un atributo
de CLASE que cuenta cuántos estudiantes se crearon. Agregar un
@classmethod total_estudiantes() que devuelva ese contador.
"""


class Estudiante:
    cantidad_estudiantes = 0  # atributo de clase: compartido por todas las instancias

    def __init__(self, nombre):
        self.nombre = nombre  # atributo de instancia: propio de cada objeto
        Estudiante.cantidad_estudiantes += 1

    @classmethod
    def total_estudiantes(cls):
        return cls.cantidad_estudiantes


e1 = Estudiante("Lucía")
e2 = Estudiante("Martín")
e3 = Estudiante("Sofía")

print(f"Estudiantes creados: {Estudiante.total_estudiantes()}")
# El atributo de clase es el mismo para todas las instancias:
print(e1.cantidad_estudiantes, e2.cantidad_estudiantes, e3.cantidad_estudiantes)
