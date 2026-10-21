class Empleado:
    cantidad_empleados = 0

    def __init__(self, nombre, sueldo_base):
        self.nombre = nombre
        self.sueldo_base = sueldo_base
        self.__ultimo_sueldo = 0
        Empleado.cantidad_empleados += 1

    @classmethod
    def total_empleados(cls):
        return cls.cantidad_empleados

    @property
    def ultimo_sueldo(self):
        return self.__ultimo_sueldo

    def _guardar_sueldo(self, importe):
        self.__ultimo_sueldo = importe

    def calcular_sueldo(self):
        raise NotImplementedError("Cada empleado debe calcular su sueldo.")


class Vendedor(Empleado):
    def calcular_sueldo(self):
        total = self.sueldo_base + 15000
        self._guardar_sueldo(total)
        return total


class Gerente(Empleado):
    def calcular_sueldo(self):
        total = self.sueldo_base + 40000
        self._guardar_sueldo(total)
        return total


empleado_ventas = Vendedor("Nicolás", 600000)
empleado_gerencia = Gerente("Martina", 850000)

lista_empleados = [empleado_ventas, empleado_gerencia]

for persona in lista_empleados:
    persona.calcular_sueldo()
    print(f"Empleado: {persona.nombre}")
    print(f"Sueldo: ${persona.ultimo_sueldo}")
    print()

print(f"Cantidad de empleados creados: {Empleado.total_empleados()}")