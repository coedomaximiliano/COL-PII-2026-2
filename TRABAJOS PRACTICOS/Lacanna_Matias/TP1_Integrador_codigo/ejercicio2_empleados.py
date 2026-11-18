# Ejercicio 2 

class Empleado:
    cantidad_empleados = 0  

    def __init__(self, nombre, sueldo_base):
        self.nombre = nombre           
        self.sueldo_base = sueldo_base
        self.__ultimo_sueldo = None    
        Empleado.cantidad_empleados += 1

    @classmethod
    def total_empleados(cls):
        return cls.cantidad_empleados

    @property
    def ultimo_sueldo(self):
        
        return self.__ultimo_sueldo

    def _guardar_sueldo(self, monto):
       
        self.__ultimo_sueldo = monto
        return monto

    def calcular_sueldo(self):
        return self._guardar_sueldo(self.sueldo_base)


class Vendedor(Empleado):
    def __init__(self, nombre, sueldo_base, ventas, comision=0.05):
        super().__init__(nombre, sueldo_base)
        self.ventas = ventas
        self.comision = comision

    def calcular_sueldo(self):
        
        return self._guardar_sueldo(self.sueldo_base + self.ventas * self.comision)


class Gerente(Empleado):
    def __init__(self, nombre, sueldo_base, bono):
        super().__init__(nombre, sueldo_base)
        self.bono = bono

    def calcular_sueldo(self):
        
        return self._guardar_sueldo(self.sueldo_base + self.bono)


if __name__ == "__main__":
    empleados = [
        Vendedor("Ana", 800000, ventas=3000000),
        Gerente("Carlos", 1200000, bono=400000),
    ]

    for e in empleados:
        e.calcular_sueldo()  
        print(f"{e.nombre} ({e.__class__.__name__}): ${e.ultimo_sueldo:,.2f}")

    print("Total de empleados creados:", Empleado.total_empleados())
