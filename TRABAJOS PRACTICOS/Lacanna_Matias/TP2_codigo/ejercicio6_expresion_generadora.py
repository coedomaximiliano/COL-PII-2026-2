# Ejercicio 6 

import sys

N = 1_000_000

suma = sum(x ** 2 for x in range(1, N + 1))
print(f"Suma de los cuadrados del 1 al {N:,}: {suma:,}")


generador = (x ** 2 for x in range(1, N + 1))
lista = [x ** 2 for x in range(1, N + 1)]
print(f"Tamaño del generador: {sys.getsizeof(generador)} bytes")
print(f"Tamaño de la lista:   {sys.getsizeof(lista):,} bytes")
