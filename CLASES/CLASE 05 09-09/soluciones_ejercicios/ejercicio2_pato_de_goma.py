"""
SOLUCIÓN — Ejercicio 2 · Herencia múltiple con mixins
(Clase 5 · al final)
"""


class Flotador:
    def flotar(self):
        print("Floto en el agua")


class ReproductorDeSonido:
    def sonar(self):
        print("¡Cuac!")


class PatoDeGoma(Flotador, ReproductorDeSonido):
    pass


if __name__ == "__main__":
    pato = PatoDeGoma()
    pato.flotar()
    pato.sonar()
