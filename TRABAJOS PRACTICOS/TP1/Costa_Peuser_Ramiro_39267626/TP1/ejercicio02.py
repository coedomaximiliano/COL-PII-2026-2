#Nómina de empleados con variable de clase
#Definí una clase Empleado con nombre y sueldo_base (variables de instancia) y una variable de CLASE cantidad_empleados que se incremente en cada constructor.
#Agregá un @classmethod llamado total_empleados() que devuelva cantidad_empleados.
#Definí dos subclases de Empleado (por ejemplo Vendedor y Gerente) que sobreescriban un método calcular_sueldo() de forma distinta (polimorfismo).
#Encapsulá el resultado del último cálculo en un atributo privado __ultimo_sueldo, expuesto de solo lectura con @property.
#Tu programa debe:
#Crear al menos un empleado de cada subclase.
#Calcular y mostrar el sueldo de cada uno accediendo a través de la property.
#Mostrar el total de empleados creados usando el classmethod.

class Empleado:
    cantidad_empleados = 0

    def __init__(self, nombre, sueldo_base):
        self.nombre = nombre
        self.sueldo_base = sueldo_base
        Empleado.cantidad_empleados += 1
        self.__ultimo_sueldo = 0

    @classmethod
    def total_empleados(cls):
        return cls.cantidad_empleados

    @property
    def ultimo_sueldo(self):
        return self.__ultimo_sueldo

    def _actualizar_sueldo(self, sueldo):
        self.__ultimo_sueldo = sueldo

    def calcular_sueldo(self):
        raise NotImplementedError


class Vendedor(Empleado):
    def calcular_sueldo(self):
        sueldo = self.sueldo_base + 1000
        self._actualizar_sueldo(sueldo)
        return sueldo


class Gerente(Empleado):
    def calcular_sueldo(self):
        sueldo = self.sueldo_base + 5000
        self._actualizar_sueldo(sueldo)
        return sueldo


# Crear empleados
vendedor = Vendedor("Juan", 50000)
gerente = Gerente("Laura", 70000)

# Polimorfismo
empleados = [vendedor, gerente]

for empleado in empleados:
    empleado.calcular_sueldo()
    print(f"{empleado.nombre}: ${empleado.ultimo_sueldo}")

print(f"Total de empleados: {Empleado.total_empleados()}")