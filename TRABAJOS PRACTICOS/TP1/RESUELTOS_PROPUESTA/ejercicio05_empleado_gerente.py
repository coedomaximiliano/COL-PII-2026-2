"""
EJERCICIO 5 (Medio) — Herencia simple: Empleado -> Gerente
Consigna: clase Empleado con nombre y sueldo_base, y un método
calcular_sueldo() que devuelve sueldo_base. Subclase Gerente que
sobreescribe calcular_sueldo() sumando un bono fijo.
"""


class Empleado:
    def __init__(self, nombre, sueldo_base):
        self.nombre = nombre
        self.sueldo_base = sueldo_base

    def calcular_sueldo(self):
        return self.sueldo_base


class Gerente(Empleado):
    BONO = 50000

    def calcular_sueldo(self):
        # Reutiliza el cálculo de la clase base y le suma el bono
        return super().calcular_sueldo() + self.BONO


e1 = Empleado("Martín", 300000)
e2 = Gerente("Sofía", 300000)

print(f"{e1.nombre} cobra ${e1.calcular_sueldo()}")
print(f"{e2.nombre} (gerenta) cobra ${e2.calcular_sueldo()}")
