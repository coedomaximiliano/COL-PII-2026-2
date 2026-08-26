"""
EJERCICIO 10 (Integrador) — Sistema de gestión de un zoológico
Consigna: combinar abstracción, herencia, polimorfismo y composición.
Clase base Animal (nombre, edad) con hacer_sonido() (a definir en cada
subclase) y descripcion(). Subclases Leon, Pinguino y Elefante. Clase
Zoologico que compone una lista de animales, con métodos agregar_animal(),
sonidos_del_dia() (recorrido polimórfico) y animal_mas_viejo().
"""


class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self):
        raise NotImplementedError("Cada especie debe definir su propio sonido")

    def descripcion(self):
        return f"{self.nombre} ({self.edad} años, {type(self).__name__})"


class Leon(Animal):
    def hacer_sonido(self):
        return "Roar"


class Pinguino(Animal):
    def hacer_sonido(self):
        return "Wak wak"


class Elefante(Animal):
    def hacer_sonido(self):
        return "Pruuum"


class Zoologico:
    def __init__(self, nombre):
        self.nombre = nombre
        self.animales = []  # composición: el zoológico "tiene" animales

    def agregar_animal(self, animal):
        self.animales.append(animal)

    def sonidos_del_dia(self):
        # Polimorfismo: no importa la clase de cada animal, todos responden
        # a hacer_sonido() a su manera.
        for animal in self.animales:
            print(f"{animal.descripcion()} → {animal.hacer_sonido()}")

    def animal_mas_viejo(self):
        return max(self.animales, key=lambda a: a.edad)


zoo = Zoologico("Zoo UAI")
zoo.agregar_animal(Leon("Simba", 5))
zoo.agregar_animal(Pinguino("Rico", 2))
zoo.agregar_animal(Elefante("Dumbo", 12))

print(f"--- Sonidos de hoy en {zoo.nombre} ---")
zoo.sonidos_del_dia()

mas_viejo = zoo.animal_mas_viejo()
print(f"\nEl animal más viejo es {mas_viejo.nombre}, con {mas_viejo.edad} años.")
