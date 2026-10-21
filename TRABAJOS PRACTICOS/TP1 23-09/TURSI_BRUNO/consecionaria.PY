#una clase con nombre y precio llamada producto
#una clase llamada carrito que mantenga una lista de productos, con un metodo, agregar_producto() y un metodo total() q sume los precios
class Producto():
    def __init__(self, Nombre, Precio):
       self.Nombre = Nombre
       self.Precio = Precio

class Carrito():
    def __init__(self, CantidadProductos,PrecioTotal):
        self.CantidadProductos = CantidadProductos
        self.PrecioTotal = PrecioTotal
        self.ProductosLista = []

        def agregar_producto(self):
          self.ProductosLista.append(Producto)
          print(f"el productos{Producto} se agrego correctamente")
 
        def total_productos(self):
         PrecioTotal = sum(prod.precio for prod in self.productos) 


Producto1 = Producto ("agua", 20000) 
Producto2 = Producto ("falopita", 289000) 
Producto3 = Producto ("coca", 25000) 

Carrito1 = Carrito() 
Carrito1.agregar_producto(Producto1)
Carrito1.agregar_producto(Producto2)
Carrito1.agregar_producto(Producto3)

Carrito1.total_productos()


