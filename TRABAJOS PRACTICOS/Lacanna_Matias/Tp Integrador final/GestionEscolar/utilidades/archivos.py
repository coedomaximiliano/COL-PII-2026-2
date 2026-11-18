"""
archivos.py
Rutas de los archivos del proyecto y funciones auxiliares para leer y escribir texto.
Las rutas se arman a partir de la ubicación de este archivo, así el programa funciona
sin importar desde qué carpeta se ejecute (consola o Visual Studio).
"""
import os

CARPETA_PROYECTO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARPETA_DATOS = os.path.join(CARPETA_PROYECTO, "datos")
CARPETA_SALIDA = os.path.join(CARPETA_PROYECTO, "salida")

RUTA_ESCUELA = os.path.join(CARPETA_DATOS, "escuela.txt")
RUTA_HISTORICOS = os.path.join(CARPETA_DATOS, "historicos.txt")
RUTA_REPORTE = os.path.join(CARPETA_SALIDA, "reporte.txt")
RUTA_LOG = os.path.join(CARPETA_SALIDA, "log.txt")


def asegurar_carpeta(ruta_archivo):
    """Crea la carpeta del archivo si no existe."""
    os.makedirs(os.path.dirname(ruta_archivo), exist_ok=True)


def agregar_linea(ruta, linea):
    """Agrega una línea al final del archivo (modo 'a')."""
    asegurar_carpeta(ruta)
    with open(ruta, "a", encoding="utf-8") as archivo:
        archivo.write(linea + "\n")


def escribir_lineas(ruta, lineas):
    """Escribe (pisando el archivo) todas las líneas que entregue un iterable o generador."""
    asegurar_carpeta(ruta)
    with open(ruta, "w", encoding="utf-8") as archivo:
        for linea in lineas:
            archivo.write(linea + "\n")
