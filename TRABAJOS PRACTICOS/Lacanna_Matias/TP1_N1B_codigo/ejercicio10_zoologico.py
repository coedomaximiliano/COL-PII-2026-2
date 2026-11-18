# Ejercicio 10 
from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @abstractmethod
    def hacer_sonido(self):
        pass

    def descripcion(self):
        return f"{self.nombre} es un {self.__class__.__name__} de {self.edad} años"


class Leon(Animal):
    def hacer_sonido(self):
        return "Grrr"


class Elefante(Animal):
    def hacer_sonido(self):
        return "Prrrr"


class Mono(Animal):
    def hacer_sonido(self):
        return "Uh uh ah ah"


class Zoologico:
    def __init__(self, nombre):
        self.nombre = nombre
        self.animales = []

    def agregar_animal(self, animal):
        self.animales.append(animal)

    def sonidos_del_dia(self):
        for a in self.animales:
            print(f"{a.descripcion()} y hace: {a.hacer_sonido()}")

    def animal_mas_viejo(self):
        if not self.animales:
            return None
        return max(self.animales, key=lambda a: a.edad)


if __name__ == "__main__":
    zoo = Zoologico("Ecoparque")
    zoo.agregar_animal(Leon("Simba", 8))
    zoo.agregar_animal(Elefante("Dumbo", 25))
    zoo.agregar_animal(Mono("Coco", 5))

    zoo.sonidos_del_dia()
    viejo = zoo.animal_mas_viejo()
    print(f"El animal más viejo es {viejo.nombre} con {viejo.edad} años")

    try:
        Animal("Genérico", 1)
    except TypeError:
        print("No se puede crear un Animal genérico: es una clase abstracta")
