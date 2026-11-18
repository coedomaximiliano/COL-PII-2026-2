# Ejercicio 3 

class Terrestre:
    def desplazarse(self):
        print("Me desplazo por tierra")


class Acuatico:
    def desplazarse(self):
        print("Me desplazo por agua")


class VehiculoAnfibio(Terrestre, Acuatico):
    def __init__(self, combustible):
        self.__combustible = combustible 

    @property
    def combustible(self):
        return self.__combustible

    def desplazarse(self):
       
        Terrestre.desplazarse(self)
        Acuatico.desplazarse(self)

    def consumir(self, litros):
        if litros <= 0:
            print("La cantidad de litros debe ser positiva")
        elif litros > self.__combustible:
            print(f"No se pueden consumir {litros} L: solo quedan {self.__combustible} L")
        else:
            self.__combustible -= litros
            print(f"Consumidos {litros} L. Quedan {self.__combustible} L")


if __name__ == "__main__":
    anfibio = VehiculoAnfibio(50)

    print("¿Es Terrestre?", isinstance(anfibio, Terrestre))
    print("¿Es Acuatico?", isinstance(anfibio, Acuatico))
    print("Orden de resolución (MRO):", [c.__name__ for c in VehiculoAnfibio.__mro__])

    anfibio.desplazarse()
    anfibio.consumir(20)
    anfibio.consumir(15)
    anfibio.consumir(100)  
