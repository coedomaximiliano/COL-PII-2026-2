# Ejercicio 4 


class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio


class Carrito:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def total(self):
        return sum(p.precio for p in self.productos)


if __name__ == "__main__":
    carrito = Carrito()
    carrito.agregar_producto(Producto("Yerba 1kg", 4500))
    carrito.agregar_producto(Producto("Galletitas", 1800))
    carrito.agregar_producto(Producto("Leche", 1500))

    print("Detalle del carrito:")
    for p in carrito.productos:
        print(f"- {p.nombre}: ${p.precio}")
    print("Total:", f"${carrito.total()}")
