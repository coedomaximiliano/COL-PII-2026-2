"""
SOLUCIÓN — Ejercicio 1 · Constructor y destructor con mensajes
(Clase 5 · a mitad de la clase)
"""


class ArchivoTemporal:
    def __init__(self, nombre):
        self.nombre = nombre
        print(f"Se abrió el archivo '{self.nombre}'")

    def __del__(self):
        print(f"Se cerró el archivo '{self.nombre}'")


if __name__ == "__main__":
    archivo = ArchivoTemporal("datos.tmp")
    print("Trabajando con el archivo...")
    del archivo  # dispara __del__ y muestra el orden de los mensajes
