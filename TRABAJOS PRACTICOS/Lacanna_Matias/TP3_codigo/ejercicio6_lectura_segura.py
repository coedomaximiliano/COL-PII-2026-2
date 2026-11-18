# Ejercicio 6 

from pathlib import Path

CARPETA = Path(__file__).parent


def leer_archivo_seguro(nombre_archivo):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Aviso: el archivo '{Path(nombre_archivo).name}' no existe. Revisá el nombre o la ruta.")
        return None


if __name__ == "__main__":
    existente = CARPETA / "datos_prueba.txt"
    with open(existente, "w", encoding="utf-8") as f:
        f.write("Primera línea del archivo\nSegunda línea del archivo\n")

    print("--- Archivo que existe ---")
    contenido = leer_archivo_seguro(existente)
    print(contenido, end="")

    print("--- Archivo que no existe ---")
    contenido = leer_archivo_seguro(CARPETA / "no_existe.txt")
    print("Valor devuelto:", contenido)

    print("El programa siguió corriendo después del error")
