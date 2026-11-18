# Ejercicio 5


class Empleado:
    def __init__(self, nombre, sueldo_base):
        self.nombre = nombre
        self.sueldo_base = sueldo_base

    def calcular_sueldo(self):
        return self.sueldo_base


class Gerente(Empleado):
    BONO = 200000  

    def calcular_sueldo(self):
        return super().calcular_sueldo() + self.BONO


if __name__ == "__main__":
    e = Empleado("Laura", 900000)
    g = Gerente("Martín", 900000)

    print(f"{e.nombre} (Empleado): ${e.calcular_sueldo()}")
    print(f"{g.nombre} (Gerente): ${g.calcular_sueldo()}")
    print("¿El sueldo del gerente incluye el bono?",
          g.calcular_sueldo() == e.calcular_sueldo() + Gerente.BONO)
