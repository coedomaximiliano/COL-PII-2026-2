class Animal():
    
    def hacer_sonido(self):
        print("sonido animal")

class Perro(Animal):
    def hacer_sonido(self):
        print("guau guau")

class Gato(Animal):
    def hacer_sonido(self):
        print("miaw miaw")
    def __del__(self):
        print("chau")

        


gato1 = Gato()
perro1 = Perro()  
gato1.hacer_sonido()
perro1.hacer_sonido()
del gato1




