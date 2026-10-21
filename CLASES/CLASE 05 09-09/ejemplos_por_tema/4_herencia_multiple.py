"""
EJEMPLO — Herencia múltiple
En Python una clase puede heredar de más de una superclase a la vez. El
orden en que se declaran las superclases define el orden de resolución
de métodos (MRO) si hay nombres repetidos.
"""


class Flotador:
    def flotar(self):
        print("Floto en el agua")


class ReproductorDeSonido:
    def hacer_sonido(self):
        print("¡Cuac!")


class PatoDeGoma(Flotador, ReproductorDeSonido):  # hereda de DOS superclases
    def __init__(self, color):
        self.color = color


pato = PatoDeGoma("amarillo")
pato.flotar()          # heredado de Flotador
pato.hacer_sonido()    # heredado de ReproductorDeSonido
print(f"Pato de goma color {pato.color}")
print("MRO:", [clase.__name__ for clase in PatoDeGoma.__mro__])
