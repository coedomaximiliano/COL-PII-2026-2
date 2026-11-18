# Ejercicio 4 
from pathlib import Path

ARCHIVO = Path(__file__).parent / "alumnos.txt"


class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def __str__(self):
        return f"Alumno(nombre={self.nombre}, nota={self.nota})"


def guardar_alumnos(alumnos, ruta):
    with open(ruta, "w", encoding="utf-8") as f:
        for a in alumnos:
            f.write(f"{a.nombre};{a.nota}\n")


def leer_alumnos(ruta):
    alumnos = []
    with open(ruta, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if linea:
                nombre, nota = linea.split(";")
                alumnos.append(Alumno(nombre, float(nota)))
    return alumnos


if __name__ == "__main__":
    lista = [Alumno("Ana", 8.5), Alumno("Bruno", 6), Alumno("Carla", 9.75)]
    guardar_alumnos(lista, ARCHIVO)
    print(f"Se guardaron {len(lista)} alumnos en {ARCHIVO.name}")

    reconstruidos = leer_alumnos(ARCHIVO)
    print("Alumnos reconstruidos desde el archivo:")
    for a in reconstruidos:
        print(" ", a)
