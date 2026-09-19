#Concesionaria de vehículos: el sistema completo
#Este último ejercicio integra los temas de las 5 clases en un mismo programa. Definí una clase base Vehiculo con marca y precio (variables de instancia), una variable de clase total_vehiculos, constructor y destructor, y un atributo privado __patente (encapsulamiento) expuesto de solo lectura con @property.
#Definí al menos tres subclases de Vehiculo (por ejemplo Auto, Moto y Camion) que hereden de forma simple y sobreescriban un método moverse() (polimorfismo).
#Elegí una de esas subclases para que además herede de una segunda clase auxiliar (por ejemplo TransporteDeCarga, con un método cargar(kg)), formando un caso de herencia múltiple.
#Implementá el método especial __add__ en Vehiculo, para que sumar dos vehículos con el operador + devuelva la suma de sus precios (otra forma de polimorfismo: sobrecarga de operadores).
#Definí una clase Concesionaria que "tenga" una lista de vehículos (composición), con un método valor_total_stock() y un método mostrar_stock() que recorra la lista llamando siempre a los mismos métodos, sin importar la subclase de cada vehículo.
#Tu programa debe:
#Cargar al menos 4 vehículos de subclases distintas en una Concesionaria.
#Mostrar la marca, la patente y el resultado de moverse() de cada vehículo (polimorfismo).
#Sumar el precio de dos vehículos usando el operador + (aprovechando __add__).
#Mostrar el valor total del stock y la cantidad total de vehículos creados (variable de clase).
#Agregar un comentario en el código explicando que, al no heredar explícitamente de ninguna clase antigua, todas las clases del ejercicio son clases de "nuevo estilo" (en Python 3 todas las clases lo son por defecto).

class Vehiculo:
    total_vehiculos = 0

    def __init__(self, marca, precio, patente):
        self.marca = marca
        self.precio = precio
        self.__patente = patente

        Vehiculo.total_vehiculos += 1

    @property
    def patente(self):
        return self.__patente

    def __del__(self):
        print(f"Vehículo {self.marca} con patente {self.__patente} eliminado.")

    def moverse(self):
        raise NotImplementedError(
            "El método moverse() debe ser implementado por las subclases."
        )

    def __add__(self, otro):
        return self.precio + otro.precio


class Auto(Vehiculo):
    def moverse(self):
        return "El auto se mueve por la calle."


class Moto(Vehiculo):
    def moverse(self):
        return "La moto se mueve por la calle."


class Camion(Vehiculo):
    def moverse(self):
        return "El camión se mueve por la ruta."


class TransporteDeCarga:
    def cargar(self, kg):
        print(f"Se cargaron {kg} kg de mercadería.")


class Camioneta(Vehiculo, TransporteDeCarga):
    def moverse(self):
        return "La camioneta se mueve por la calle."

    # Puede utilizar el método cargar() heredado de TransporteDeCarga.


class Concesionaria:
    def __init__(self):
        self.vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def valor_total_stock(self):
        total = 0

        for vehiculo in self.vehiculos:
            total += vehiculo.precio

        return total

    def mostrar_stock(self):
        for vehiculo in self.vehiculos:
            print("-" * 40)
            print(f"Marca: {vehiculo.marca}")
            print(f"Patente: {vehiculo.patente}")
            print(f"Movimiento: {vehiculo.moverse()}")
            


# Crear la concesionaria
concesionaria = Concesionaria()

# Crear vehículos
auto = Auto("Toyota", 20000, "AA123AA")
moto = Moto("Honda", 10000, "AB456AB")
camion = Camion("Mercedes-Benz", 50000, "AC789AC")
camioneta = Camioneta("Ford", 30000, "AD321AD")

# Agregar los vehículos a la concesionaria
concesionaria.agregar_vehiculo(auto)
concesionaria.agregar_vehiculo(moto)
concesionaria.agregar_vehiculo(camion)
concesionaria.agregar_vehiculo(camioneta)


# Mostrar información del stock
print("STOCK DE LA CONCESIONARIA:")
concesionaria.mostrar_stock()


# Utilizar la herencia múltiple
print("TRANSPORTE DE CARGA:")
print("-" * 40)
camioneta.cargar(1500)


# Sobrecarga del operador +
print("\nSUMA DE PRECIOS:")
print("-" * 40)
suma = auto + moto
print(f"Precio del auto + precio de la moto: ${suma}")


# Valor total del stock
print("\nTOTAL DEL STOCK:")
print("-" * 40)
print(f"Valor total: ${concesionaria.valor_total_stock()}")


# Variable de clase
print("\nTOTAL DE VEHÍCULOS CREADOS:")
print("-" * 40)
print(f"Cantidad total: {Vehiculo.total_vehiculos}")