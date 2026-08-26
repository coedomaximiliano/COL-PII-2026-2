"""
EJERCICIO 6 (Medio) — Herencia + polimorfismo: Animal -> Perro/Gato/Vaca
Consigna: clase base Animal con un método hacer_sonido(). Subclases Perro,
Gato y Vaca que lo sobreescriben. Guardarlos en una misma lista y
recorrerla llamando a hacer_sonido() en cada uno (polimorfismo).
"""


class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        raise NotImplementedError("Cada animal debe definir su propio sonido")


class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"


class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"


class Vaca(Animal):
    def hacer_sonido(self):
        return "Muu"


animales = [Perro("Toby"), Gato("Michi"), Vaca("Clarabela")]

for animal in animales:
    # No importa de qué clase es cada uno: todos responden a hacer_sonido()
    print(f"{animal.nombre} dice: {animal.hacer_sonido()}")
