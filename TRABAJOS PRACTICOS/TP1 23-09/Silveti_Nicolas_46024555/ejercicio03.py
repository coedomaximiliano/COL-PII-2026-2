class Terrestre:
    def desplazarse(self):
        print("Me desplazo por tierra")


class Acuatico:
    def desplazarse(self):
        print("Me desplazo por agua")


class VehiculoAnfibio(Terrestre, Acuatico):
    def __init__(self, combustible):
        if combustible < 0:
            raise ValueError("El combustible inicial no puede ser negativo.")
        self.__combustible = combustible

    def desplazarse(self):
        Terrestre.desplazarse(self)
        Acuatico.desplazarse(self)

    def consumir(self, litros):
        if litros <= 0:
            print("La cantidad a consumir debe ser mayor que cero.")
        elif litros > self.__combustible:
            disponible = self.__combustible
            self.__combustible = 0
            print(f"No alcanza el combustible. Se consumieron {disponible} litros.")
        else:
            self.__combustible -= litros
            print(f"Se consumieron {litros} litros.")

        print(f"Combustible restante: {self.__combustible} litros")


vehiculo = VehiculoAnfibio(60)

# Comprobar que pertenece a ambas clases
print(f"Es terrestre: {isinstance(vehiculo, Terrestre)}")
print(f"Es acuático: {isinstance(vehiculo, Acuatico)}")

# Ejecutar el comportamiento de ambas clases
vehiculo.desplazarse()

# Probar distintos consumos
vehiculo.consumir(15)
vehiculo.consumir(25)
vehiculo.consumir(30)