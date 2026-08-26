"""
EJERCICIO INTEGRADOR — Abstracción + Objetos/Clases + Herencia + Polimorfismo
Consigna: armar un sistema de una concesionaria que use los 4 conceptos
de la Clase 3, cada uno señalado en un comentario para que sea fácil
identificarlo.
"""

# ------------------------------------------------------------------
# 1) ABSTRACCIÓN
# Un vehículo real tiene muchísimos datos posibles (color, kilometraje,
# dueños anteriores, etc). Para el sistema de una concesionaria, lo único
# relevante es: marca, precio y cómo se mueve. Todo lo demás se descarta.
# ------------------------------------------------------------------


# ------------------------------------------------------------------
# 2) CLASES Y OBJETOS + 3) HERENCIA
# Vehiculo es la superclase (el molde común). Auto, Moto y Bicicleta son
# subclases que heredan marca y precio, y sobreescriben moverse().
# ------------------------------------------------------------------
class Vehiculo:
    def __init__(self, marca, precio):
        self.marca = marca
        self.precio = precio

    def moverse(self):
        return "Me muevo"

    def info(self):
        return f"{type(self).__name__} {self.marca} — ${self.precio}"


class Auto(Vehiculo):
    def __init__(self, marca, precio, puertas):
        super().__init__(marca, precio)
        self.puertas = puertas

    def moverse(self):
        return "Ando sobre 4 ruedas"


class Moto(Vehiculo):
    def __init__(self, marca, precio, cilindrada):
        super().__init__(marca, precio)
        self.cilindrada = cilindrada

    def moverse(self):
        return "Ando sobre 2 ruedas a motor"


class Bicicleta(Vehiculo):
    def moverse(self):
        return "Ando a pedal"


# ------------------------------------------------------------------
# Concesionaria: compone (contiene) una lista de vehículos de distintas
# clases, todas hijas de Vehiculo.
# ------------------------------------------------------------------
class Concesionaria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vehiculos = []

    def agregar(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def valor_total_stock(self):
        return sum(v.precio for v in self.vehiculos)

    # ------------------------------------------------------------------
    # 4) POLIMORFISMO
    # Recorremos vehículos de clases distintas (Auto, Moto, Bicicleta) y
    # llamamos siempre a los mismos métodos, info() y moverse(). Cada
    # objeto responde a su manera, sin que este código sepa de qué clase
    # es cada uno.
    # ------------------------------------------------------------------
    def mostrar_stock(self):
        print(f"--- Stock de {self.nombre} ---")
        for v in self.vehiculos:
            print(f"{v.info()} → {v.moverse()}")


concesionaria = Concesionaria("Motor UAI")
concesionaria.agregar(Auto("Toyota", 25000000, puertas=4))
concesionaria.agregar(Moto("Honda", 3500000, cilindrada=150))
concesionaria.agregar(Bicicleta("Bianchi", 400000))

concesionaria.mostrar_stock()
print(f"Valor total del stock: ${concesionaria.valor_total_stock()}")
