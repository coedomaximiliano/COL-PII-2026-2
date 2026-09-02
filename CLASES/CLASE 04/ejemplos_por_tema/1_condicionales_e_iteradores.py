"""
EJEMPLO — Condicionales e iteradores dentro de métodos de una clase
Muestra cómo if/else y for/while pueden usarse dentro de los métodos de un
objeto para tomar decisiones y recorrer datos guardados como atributos.
"""


class Carrito:
    def __init__(self):
        self.items = []  # lista guardada como atributo de instancia

    def agregar(self, producto, precio):
        self.items.append((producto, precio))

    def total(self):
        # ITERADOR: recorremos los items guardados en el propio objeto
        suma = 0
        for producto, precio in self.items:
            suma += precio
        return suma

    def aplicar_descuento(self):
        # CONDICIONAL: el comportamiento depende del estado del objeto
        total = self.total()
        if total > 50000:
            return total * 0.9  # 10% de descuento
        else:
            return total


carrito = Carrito()
carrito.agregar("Notebook", 400000)
carrito.agregar("Mouse", 8000)

print(f"Total sin descuento: ${carrito.total()}")
print(f"Total con descuento aplicado: ${carrito.aplicar_descuento()}")
