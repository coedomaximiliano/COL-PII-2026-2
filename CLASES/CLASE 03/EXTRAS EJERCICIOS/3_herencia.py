"""
EJERCICIOS — HERENCIA
Recordá: una subclase reutiliza los atributos y métodos de su superclase,
y puede sobreescribir (override) los que necesite comportarse distinto.
Usa super() para llamar a la versión de la superclase desde la subclase.
"""

# ============================================================
# Ejercicio 1 (Fácil)
# Definí una clase Vehiculo con atributo marca y método moverse() que
# imprime "Me muevo". Definí una subclase Moto que herede de Vehiculo y
# agregue un atributo propio cilindrada (no necesita sobreescribir nada).
# ============================================================


class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def moverse(self):
        print("Me muevo")


class Moto(Vehiculo):
    def __init__(self, marca, cilindrada):
        super().__init__(marca)  # reutiliza el __init__ de Vehiculo
        self.cilindrada = cilindrada


moto1 = Moto("Honda", 150)
moto1.moverse()
print(f"{moto1.marca} — {moto1.cilindrada}cc")


# ============================================================
# Ejercicio 2 (Medio)
# Definí una clase Empleado con nombre y sueldo_base, y un método
# calcular_sueldo() que devuelve sueldo_base. Definí una subclase
# Vendedor que agregue un atributo comision y SOBREESCRIBA
# calcular_sueldo() para sumarle la comisión al sueldo base (usando
# super() para no repetir el cálculo del sueldo base).
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


v1 = Vendedor("Lucía", 250000, comision=40000)
print(f"{v1.nombre} cobra ${v1.calcular_sueldo()}")


# ============================================================
# Ejercicio 3 (Difícil)
# Definí una clase base Figura con un método area() que lance
# NotImplementedError. Definí tres subclases: Cuadrado, Rectangulo y
# Triangulo, cada una con sus propios atributos y su propia
# implementación de area().
# ============================================================


class Figura:
    def area(self):
        raise NotImplementedError("Cada figura debe implementar su propio cálculo de área")


class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2


class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2


for figura in [Cuadrado(4), Rectangulo(3, 5), Triangulo(6, 2)]:
    print(f"{type(figura).__name__}: área = {figura.area()}")
