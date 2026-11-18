# Ejercicio 1 
cuadrado = lambda x: x ** 2
es_par = lambda x: x % 2 == 0

numeros = [1, 2, 3, 4, 5, 10, 15]

for n in numeros:
    print(f"{n:>3} -> cuadrado: {cuadrado(n):>4} | ¿es par?: {es_par(n)}")
