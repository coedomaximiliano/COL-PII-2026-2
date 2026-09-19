#Animales (herencia + polimorfismo)
#Definí una clase base Animal con un método hacer_sonido().
#Definí al menos tres subclases (por ejemplo Perro, Gato y Vaca) que sobreescriban hacer_sonido() con su propio sonido.
#Tu programa debe:
#Guardar instancias de las distintas subclases en una misma lista.
#Recorrer la lista llamando a hacer_sonido() en cada una, sin preguntar de qué clase es cada animal (polimorfismo).

class Animal:
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        print("Guau!")

class Gato(Animal):
    def hacer_sonido(self):
        print("Miau!")

class Vaca(Animal):
    def hacer_sonido(self):
        print("Muu!")

animales = [] 
animales.append(Perro())
animales.append(Gato()) 
animales.append(Vaca()) 
for animal in animales:{animal.hacer_sonido()}