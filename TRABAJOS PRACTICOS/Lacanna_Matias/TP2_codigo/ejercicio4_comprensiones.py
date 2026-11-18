# Ejercicio 4 

DESCUENTO = 0.10
productos = [("Teclado", 25000), ("Mouse", 12000), ("Monitor", 180000), ("Auriculares", 35000)]

precios_con_descuento = [round(precio * (1 - DESCUENTO), 2) for _, precio in productos]
dicc_descuento = {nombre: round(precio * (1 - DESCUENTO), 2) for nombre, precio in productos}

print("Productos originales:", productos)
print("Lista con 10% de descuento:", precios_con_descuento)
print("Diccionario nombre -> precio con descuento:")
for nombre, precio in dicc_descuento.items():
    print(f"  {nombre}: ${precio}")
