"""
SOLUCIÓN — Ejercicio 3 · Integrador · Robots con ciclo de vida y mixins
(Clase 5 · al final de todo)

Integra: constructor y destructor + herencia múltiple (mixins) +
herencia simple (RobotAvanzado hereda de Robot).
"""


class Movil:
    def moverse(self):
        print("Me desplazo")


class Comunicable:
    def hablar(self):
        print("Emito un sonido")


class Robot(Movil, Comunicable):  # herencia múltiple: combina ambos mixins
    def __init__(self, nombre):
        self.nombre = nombre
        print(f"[ENCENDIDO] {self.nombre}")

    def __del__(self):
        print(f"[APAGADO] {self.nombre}")


class RobotAvanzado(Robot):  # herencia simple: extiende a Robot
    def __init__(self, nombre, version):
        super().__init__(nombre)
        self.version = version


if __name__ == "__main__":
    r2d2 = RobotAvanzado("R2D2", version=2.0)

    r2d2.moverse()  # heredado del mixin Movil
    r2d2.hablar()   # heredado del mixin Comunicable
    print(f"{r2d2.nombre} — versión {r2d2.version}")

    del r2d2  # dispara __del__, heredado de Robot
