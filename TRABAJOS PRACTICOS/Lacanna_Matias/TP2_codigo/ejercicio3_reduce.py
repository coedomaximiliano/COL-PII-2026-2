# Ejercicio 3 
from functools import reduce

precios = [4500, 1800, 12999, 1500, 7300]

total = reduce(lambda acum, p: acum + p, precios, 0)
mas_caro = reduce(lambda a, b: a if a > b else b, precios)

print("Precios del carrito:", precios)
print("Total de la compra: $", total)
print("Precio más caro:    $", mas_caro)
