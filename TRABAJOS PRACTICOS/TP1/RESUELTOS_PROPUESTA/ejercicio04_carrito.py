"""
EJERCICIO 4 (Medio) — Composición: Carrito de compras
Consigna: clase Producto (nombre, precio). Clase Carrito que mantiene una
lista de productos, con métodos agregar_producto(producto) y total().
Esto es COMPOSICIÓN: el Carrito "tiene" Productos, no hereda de ellos.
"""


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


carrito = Carrito()
carrito.agregar_producto(Producto("Cuaderno", 1500))
carrito.agregar_producto(Producto("Lapicera", 800))
carrito.agregar_producto(Producto("Mochila", 12000))

for p in carrito.productos:
    print(f"- {p.nombre}: ${p.precio}")
print(f"Total del carrito: ${carrito.total()}")
