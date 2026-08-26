"""
EJERCICIOS — POLIMORFISMO
Recordá: el polimorfismo permite que objetos de distintas clases
respondan de forma diferente a un mismo método. El código que llama al
método no necesita saber de qué clase es cada objeto.
"""

# ============================================================
# Ejercicio 1 (Fácil)
# Definí una clase base Instrumento con un método tocar(). Definí las
# subclases Guitarra, Piano y Bateria, cada una con su propia versión de
# tocar(). Guardalas en una lista y recorrela llamando a tocar() en cada
# una, sin preguntar de qué clase es cada instrumento.
# ============================================================


class Instrumento:
    def tocar(self):
        raise NotImplementedError


class Guitarra(Instrumento):
    def tocar(self):
        return "Rasguea las cuerdas"


class Piano(Instrumento):
    def tocar(self):
        return "Presiona las teclas"


class Bateria(Instrumento):
    def tocar(self):
        return "Golpea los parches"


banda = [Guitarra(), Piano(), Bateria()]
for instrumento in banda:
    print(f"{type(instrumento).__name__}: {instrumento.tocar()}")


# ============================================================
# Ejercicio 2 (Medio)
# Definí una clase base Forma con un método area(). Definí las subclases
# Circulo y Cuadrado, cada una con su propio cálculo de área. Recorré una
# lista de formas distintas y sumá el área total, sin importar de qué
# clase es cada una (polimorfismo).
# ============================================================

import math


class Forma:
    def area(self):
        raise NotImplementedError


class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2


class Cuadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2


formas = [Circulo(2), Cuadrado(3), Circulo(1)]
area_total = sum(f.area() for f in formas)
print(f"Área total: {area_total:.2f}")


# ============================================================
# Ejercicio 3 (Difícil)
# Definí una clase base Empleado con nombre, sueldo_base y un método
# calcular_sueldo(). Definí las subclases Vendedor (suma comisión) y
# Gerente (suma un bono fijo), cada una sobreescribiendo
# calcular_sueldo(). Calculá la NÓMINA TOTAL de una lista de empleados de
# distintas clases, llamando siempre al mismo método calcular_sueldo().
# ============================================================


class Empleado:
    def __init__(self, nombre, sueldo_base):
        self.nombre = nombre
        self.sueldo_base = sueldo_base

    def calcular_sueldo(self):
        return self.sueldo_base


class Vendedor(Empleado):
    def __init__(self, nombre, sueldo_base, comision):
        super().__init__(nombre, sueldo_base)
        self.comision = comision

    def calcular_sueldo(self):
        return super().calcular_sueldo() + self.comision


class Gerente(Empleado):
    BONO = 60000

    def calcular_sueldo(self):
        return super().calcular_sueldo() + self.BONO


plantel = [
    Empleado("Ana", 280000),
    Vendedor("Martín", 250000, comision=40000),
    Gerente("Sofía", 350000),
]

nomina_total = 0
for empleado in plantel:
    sueldo = empleado.calcular_sueldo()  # mismo llamado para las 3 clases
    print(f"{empleado.nombre} ({type(empleado).__name__}): ${sueldo}")
    nomina_total += sueldo

print(f"Nómina total: ${nomina_total}")
