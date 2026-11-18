# Ejercicio 7 

import time
from functools import wraps


def mide_tiempo(funcion):
    @wraps(funcion)
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = funcion(*args, **kwargs)
        fin = time.perf_counter()
        print(f"[mide_tiempo] {funcion.__name__} tardó {fin - inicio:.6f} segundos")
        return resultado
    return wrapper


@mide_tiempo
def sumar_hasta(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


if __name__ == "__main__":
    resultado = sumar_hasta(5_000_000)
    print("Resultado:", f"{resultado:,}")
