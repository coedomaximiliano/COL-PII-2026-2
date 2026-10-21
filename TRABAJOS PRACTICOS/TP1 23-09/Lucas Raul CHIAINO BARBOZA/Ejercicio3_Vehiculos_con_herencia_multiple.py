# Ejercicio 3: Vehiculos con herencia multiple


# Clase base que representa el desplazamiento por tierra.
class Terrestre:
    def desplazarse(self):
        print("Me desplazo por tierra")


# Clase base que representa el desplazamiento por agua.
class Acuatico:
    def desplazarse(self):
        print("Me desplazo por agua")


# Hereda de las dos clases base: es terrestre y acuatico.
class VehiculoAnfibio(Terrestre, Acuatico):
    def __init__(self, combustible):
        # Atributo privado: solo la clase controla su valor.
        self.__combustible = combustible

    def desplazarse(self):
        # Invocamos el comportamiento de ambas clases base.
        Terrestre.desplazarse(self)
        Acuatico.desplazarse(self)

    def consumir(self, litros):
        # El combustible nunca puede quedar por debajo de cero.
        self.__combustible = max(0, self.__combustible - litros)
        print(f"Combustible disponible: {self.__combustible} litros")


# Creamos un vehiculo anfibio con 100 litros de combustible.
vehiculo = VehiculoAnfibio(100)

# Comprobamos que pertenece a las dos clases base.
print(f"Es terrestre: {isinstance(vehiculo, Terrestre)}")
print(f"Es acuatico: {isinstance(vehiculo, Acuatico)}")

# El vehiculo puede desplazarse por tierra y por agua.
vehiculo.desplazarse()

# Probamos consumos normales y uno superior al combustible disponible.
vehiculo.consumir(30)
vehiculo.consumir(50)
vehiculo.consumir(40)
