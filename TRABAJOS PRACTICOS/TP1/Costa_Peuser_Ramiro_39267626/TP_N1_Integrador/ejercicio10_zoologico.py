#Este ejercicio integra todo lo trabajado en el TP. Definí una clase base Animal con nombre y edad, un método hacer_sonido() (sin implementación concreta) y un método descripcion().
#Definí al menos tres subclases de Animal, cada una con su propio hacer_sonido().
#Definí una clase Zoologico que mantenga una lista de animales (composición), con un método agregar_animal(), un método sonidos_del_dia() que recorra la lista polimórficamente, y un método animal_mas_viejo() que devuelva el animal de mayor edad.
#Tu programa debe:
#Cargar al menos tres animales de especies distintas al zoológico.
#Mostrar la descripción y el sonido de cada animal.
#Mostrar cuál es el animal más viejo.

class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self):
        pass

    def descripcion(self):
        return f"{self.nombre}, {self.edad} años"

class mono(Animal):
    def hacer_sonido(self):
        return "Ooh ooh aah aah"

class elefante(Animal):
    def hacer_sonido(self):
        return "prrrrf!"

class loro(Animal):
    def hacer_sonido(self):
        return "hola hola!"

class Zoologico:
    def __init__(self):
        self.animales = []

    def agregar_animal(self, animal):
        self.animales.append(animal)

    def sonidos(self):
        for animal in self.animales:
            print(f"{animal.descripcion()}: {animal.hacer_sonido()}")

    def animal_mas_viejo(self):
        mas_viejo = self.animales[0]
        for animal in self.animales:
            if animal.edad > mas_viejo.edad:
                mas_viejo = animal
        return mas_viejo


zoo= Zoologico()
mono1=mono("Mono", 5)
elefante1=elefante("Elefante", 10)
loro1=loro("Loro", 3)
zoo.agregar_animal(mono1) 
zoo.agregar_animal(elefante1)
zoo.agregar_animal(loro1)

zoo.sonidos()
print("El animal más viejo es:", zoo.animal_mas_viejo().descripcion())