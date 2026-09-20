#Vehículos con herencia múltiple
#Definí dos clases independientes: Terrestre (con un método desplazarse() que imprime "Me desplazo por tierra") y Acuatico (con desplazarse() que imprime "Me desplazo por agua").
#Definí una clase VehiculoAnfibio que herede de AMBAS clases (herencia múltiple) y sobreescriba desplazarse() combinando el comportamiento de las dos (podés invocar los métodos de ambas clases base desde el método sobreescrito).
#Agregale un atributo privado __combustible (encapsulamiento), inicializado por constructor, y un método consumir(litros) que lo descuente sin permitir que quede en negativo.
#Tu programa debe:

#Crear un VehiculoAnfibio y comprobar con isinstance() que es a la vez instancia de Terrestre y de Acuatico.
#Llamar a desplazarse() y a consumir() con distintos valores, incluyendo uno que supere el combustible disponible.




class Terrestre:
    def desplazarse(self):
        print("Me desplazo por tierra")


class Acuatico:
    def desplazarse(self):
        print("Me desplazo por agua")


class VehiculoAnfibio(Terrestre, Acuatico):
    def __init__(self, combustible):
        self.__combustible = combustible

    def desplazarse(self):
        Terrestre.desplazarse(self)
        Acuatico.desplazarse(self)

    def consumir(self, litros):
        if litros <= 0:
            print("La cantidad a consumir debe ser mayor que 0.")
        elif litros > self.__combustible:
            consumo = litros - self.__combustible
            self.__combustible = 0
            print(f"No hay suficiente combustible disponible. Se consumieron {consumo} litros.")
        else:
            self.__combustible -= litros

        print(f"Combustible restante: {self.__combustible} litros")


# Crear un vehículo anfibio
anfibio = VehiculoAnfibio(50)

# Comprobar herencia múltiple
print("Es instancia de Terrestre" if isinstance(anfibio, Terrestre) else "No es instancia de Terrestre")
print("Es instancia de Acuatico" if isinstance(anfibio, Acuatico) else "No es instancia de Acuatico")

# Desplazamiento
anfibio.desplazarse()

# Consumo de combustible
anfibio.consumir(10)
anfibio.consumir(20)
anfibio.consumir(30)  # Supera el combustible disponible