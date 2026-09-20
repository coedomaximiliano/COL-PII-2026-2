#Definí una clase Empleado con atributos nombre y sueldo_base, y un método calcular_sueldo() que devuelva sueldo_base.
#Definí una subclase Gerente que herede de Empleado y sobreescriba calcular_sueldo() para sumarle un bono fijo al sueldo base.
#Tu programa debe:
#Crear un Empleado y un Gerente con el mismo sueldo_base.
#Mostrar el sueldo calculado de cada uno y verificar que el del Gerente incluya el bono.

class Empleado:
    def __init__(self, nombre, sueldo_base):
        self.nombre = nombre
        self.sueldo_base = sueldo_base

    def calcular_sueldo(self):
        return self.sueldo_base

class Gerente(Empleado):
    def __init__(self, nombre, sueldo_base, bono):
        super().__init__(nombre, sueldo_base)
        self.bono = bono

    def calcular_sueldo(self):
        return self.sueldo_base + self.bono


empleado = Empleado("Juan", 500000) 
gerente = Gerente("Carlos", 500000, 100000) 
print("Sueldo de", empleado.nombre, ":", empleado.calcular_sueldo()) 
print("Sueldo de", gerente.nombre, ":", gerente.calcular_sueldo())