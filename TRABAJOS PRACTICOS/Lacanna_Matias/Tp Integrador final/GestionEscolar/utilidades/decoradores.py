"""
decoradores.py
Decoradores del sistema:
- mide_tiempo: muestra cuánto tardó la función decorada.
- registrar_operacion: agrega una línea a salida/log.txt cada vez que se ejecuta la función.
"""
import time
from datetime import datetime
from functools import wraps

from utilidades.archivos import RUTA_LOG, agregar_linea


def mide_tiempo(funcion):
    """Mide y muestra el tiempo de ejecución de la función decorada."""
    @wraps(funcion)
    def envoltura(*args, **kwargs):
        inicio = time.perf_counter()
        try:
            return funcion(*args, **kwargs)
        finally:
            duracion_ms = (time.perf_counter() - inicio) * 1000
            print(f"  [TIEMPO] {funcion.__name__} tardó {duracion_ms:.3f} ms")
    return envoltura


def registrar_operacion(funcion):
    """Registra en log.txt (modo 'a') fecha, operación, argumentos y resultado (OK o ERROR)."""
    @wraps(funcion)
    def envoltura(*args, **kwargs):
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # args[0] es el objeto (self) dueño del método; se muestra con str()
        argumentos = ", ".join(str(a) for a in args)
        try:
            resultado = funcion(*args, **kwargs)
        except Exception as error:
            agregar_linea(RUTA_LOG, f"{fecha} | {funcion.__name__}({argumentos}) | ERROR: {error}")
            raise
        agregar_linea(RUTA_LOG, f"{fecha} | {funcion.__name__}({argumentos}) | OK")
        return resultado
    return envoltura
