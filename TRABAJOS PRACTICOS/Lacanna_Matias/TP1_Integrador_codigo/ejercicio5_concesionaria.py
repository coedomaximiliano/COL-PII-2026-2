# Ejercicio 5 


class Vehiculo:
    total_vehiculos = 0  

    def __init__(self, marca, precio, patente):
        self.marca = marca          
        self.precio = precio
        self.__patente = patente    
        Vehiculo.total_vehiculos += 1

    def __del__(self):
        print(f"Se dio de baja el vehículo {self.__patente}")

    @property
    def patente(self):
        return self.__patente

    def moverse(self):
        raise NotImplementedError("Cada subclase define cómo se mueve")

    def __add__(self, otro):
        
        if isinstance(otro, Vehiculo):
            return self.precio + otro.precio
        return NotImplemented


class TransporteDeCarga:
  
    def __init__(self, capacidad_kg):
        self.capacidad_kg = capacidad_kg
        self.carga_actual = 0

    def cargar(self, kg):
        if self.carga_actual + kg > self.capacidad_kg:
            print(f"No se pueden cargar {kg} kg: con {self.carga_actual} kg ya cargados "
                  f"se supera la capacidad de {self.capacidad_kg} kg")
        else:
            self.carga_actual += kg
            print(f"Cargados {kg} kg. Carga actual: {self.carga_actual} kg")


class Auto(Vehiculo):
    def moverse(self):
        return "Avanza por la ruta sobre 4 ruedas"


class Moto(Vehiculo):
    def moverse(self):
        return "Avanza esquivando el tránsito sobre 2 ruedas"


class Camion(Vehiculo, TransporteDeCarga):
   
    def __init__(self, marca, precio, patente, capacidad_kg):
        Vehiculo.__init__(self, marca, precio, patente)
        TransporteDeCarga.__init__(self, capacidad_kg)

    def moverse(self):
        return f"Avanza despacio por la autopista con {self.carga_actual} kg de carga"


class Concesionaria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vehiculos = [] 

    def agregar(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def valor_total_stock(self):
        return sum(v.precio for v in self.vehiculos)

    def mostrar_stock(self):
        print(f"--- Stock de {self.nombre} ---")
        for v in self.vehiculos:
          
            print(f"{v.__class__.__name__:7} | {v.marca:10} | {v.patente} | {v.moverse()}")


if __name__ == "__main__":
    c = Concesionaria("AutoSur")
    c.agregar(Auto("Toyota", 25000000, "AE123BC"))
    c.agregar(Auto("Chevrolet", 22000000, "AF456DE"))
    c.agregar(Moto("Honda", 6000000, "A123BCD"))
    camion = Camion("Scania", 90000000, "AD789FG", capacidad_kg=10000)
    c.agregar(camion)

    camion.cargar(4000)
    camion.cargar(8000)  

    c.mostrar_stock()

    v1, v2 = c.vehiculos[0], c.vehiculos[2]
    print(f"{v1.marca} + {v2.marca} = ${v1 + v2:,}")
    print(f"Valor total del stock: ${c.valor_total_stock():,}")
    print("Vehículos creados:", Vehiculo.total_vehiculos)
    print("¿El camión es TransporteDeCarga?", isinstance(camion, TransporteDeCarga))
    print("Fin del programa (al cerrarse se ejecutan los destructores):")
