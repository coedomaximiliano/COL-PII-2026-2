"""
EJEMPLO — Herencia simple
Una subclase extiende UNA única superclase. Con super() se puede llamar
a la implementación de la superclase y agregar comportamiento propio, en
vez de reescribirla desde cero.
"""


class Empleado:
    def __init__(self, nombre, sueldo_base):
        self.nombre = nombre
        self.sueldo_base = sueldo_base

    def calcular_sueldo(self):
        return self.sueldo_base


class Vendedor(Empleado):  # hereda de UNA sola superclase
    def __init__(self, nombre, sueldo_base, comision):
        super().__init__(nombre, sueldo_base)
        self.comision = comision

    def calcular_sueldo(self):
        return super().calcular_sueldo() + self.comision


vendedor = Vendedor("Lucía", 250000, comision=40000)
print(f"{vendedor.nombre} cobra ${vendedor.calcular_sueldo()}")
