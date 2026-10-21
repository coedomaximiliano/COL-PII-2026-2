# En Python 3 todas las clases son de nuevo estilo:
# heredan de object directa o indirectamente, aunque no se escriba.

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
        print(f"Se eliminó el vehículo {self.marca}, patente {self.__patente}.")

    def moverse(self):
        raise NotImplementedError("Cada vehículo debe definir cómo moverse.")

    def __add__(self, otro):
        return self.precio + otro.precio


class Auto(Vehiculo):
    def moverse(self):
        return "El auto circula por la ciudad."


class Moto(Vehiculo):
    def moverse(self):
        return "La moto circula por las calles."


class Camion(Vehiculo):
    def moverse(self):
        return "El camión circula por la ruta."


class TransporteDeCarga:
    def cargar(self, kg):
        print(f"Se cargaron {kg} kg de mercadería.")


class Camioneta(Vehiculo, TransporteDeCarga):
    def moverse(self):
        return "La camioneta circula por caminos rurales."


class Concesionaria:
    def __init__(self):
        self.vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def valor_total_stock(self):
        importe_total = 0
        for unidad in self.vehiculos:
            importe_total += unidad.precio
        return importe_total

    def mostrar_stock(self):
        for unidad in self.vehiculos:
            print(f"Marca: {unidad.marca}")
            print(f"Patente: {unidad.patente}")
            print(f"Movimiento: {unidad.moverse()}")
            print()


# Crear la concesionaria y los vehículos
agencia = Concesionaria()

auto_venta = Auto("Fiat", 18000, "AE123BC")
moto_venta = Moto("Yamaha", 8000, "A456DEF")
camion_venta = Camion("Scania", 65000, "AF789GH")
camioneta_venta = Camioneta("Volkswagen", 35000, "AG321JK")

# Incorporar los vehículos al stock
agencia.agregar_vehiculo(auto_venta)
agencia.agregar_vehiculo(moto_venta)
agencia.agregar_vehiculo(camion_venta)
agencia.agregar_vehiculo(camioneta_venta)

# Polimorfismo
print("VEHÍCULOS DISPONIBLES")
agencia.mostrar_stock()

# Herencia múltiple
print("CARGA DE MERCADERÍA")
camioneta_venta.cargar(900)

# Sobrecarga del operador +
precio_combinado = auto_venta + moto_venta
print(f"\nPrecio del auto y la moto: ${precio_combinado}")

# Valor del stock y cantidad de vehículos
print(f"Valor total del stock: ${agencia.valor_total_stock()}")
print(f"Vehículos creados: {Vehiculo.total_vehiculos}")