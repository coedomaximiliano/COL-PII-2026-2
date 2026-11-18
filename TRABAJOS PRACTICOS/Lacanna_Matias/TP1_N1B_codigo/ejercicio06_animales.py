# Ejercicio 6 


class Animal:
    def hacer_sonido(self):
        return "..."


class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"


class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"


class Vaca(Animal):
    def hacer_sonido(self):
        return "Muu"


if __name__ == "__main__":
    animales = [Perro(), Gato(), Vaca()]
    for a in animales:
        print(f"{a.__class__.__name__}: {a.hacer_sonido()}")
