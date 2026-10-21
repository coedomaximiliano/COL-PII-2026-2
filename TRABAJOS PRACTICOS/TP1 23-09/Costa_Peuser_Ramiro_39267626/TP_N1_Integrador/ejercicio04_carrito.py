#Definí una clase Producto con atributos nombre y precio.
#Definí una clase Carrito que mantenga una lista de productos, con un método agregar_producto(producto) y un método total() que sume los precios.
#Este es un ejemplo de composición: el Carrito "tiene" Productos, no hereda de ellos.
#Tu programa debe:
#Agregar al menos 3 productos distintos al carrito.
#Mostrar el detalle de cada producto y el total final.

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
        return sum(producto.precio for producto in self.productos)

# Crear productos
producto1 = Producto("Manzana", 10)
producto2 = Producto("Banana", 5)
producto3 = Producto("Naranja", 8)

# Crear carrito y agregar productos
carrito = Carrito()
carrito.agregar_producto(producto1)
carrito.agregar_producto(producto2)
carrito.agregar_producto(producto3)

# Mostrar detalle de cada producto
print("Detalle de productos en el carrito:")
for producto in carrito.productos:
    print(f"Producto: {producto.nombre}, Precio: {producto.precio}")
# Mostrar total final
print(f"Total final: {carrito.total()}")