"""
SOLUCIÓN — Ejercicio 2 · Contador de instancias con variable de clase
(Diapositiva "EJERCICIO 2 · INDIVIDUAL" de la Clase 4)

Consigna: Completá la clase para que cuente automáticamente cuántos
objetos Usuario se crearon, usando una variable de clase.
"""


class Usuario:
    total = 0  # variable de clase: la comparten todas las instancias

    def __init__(self, nombre):
        self.nombre = nombre
        Usuario.total += 1  # cada vez que se crea un Usuario, se incrementa


if __name__ == "__main__":
    u1 = Usuario("Ana")
    u2 = Usuario("Luis")
    u3 = Usuario("Martín")

    print(f"Se crearon {Usuario.total} usuarios")   # 3
    print(f"u1.total también ve el mismo valor: {u1.total}")  # 3
