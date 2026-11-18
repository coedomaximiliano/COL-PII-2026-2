# Ejercicio 8
 
import re
from pathlib import Path

CARPETA = Path(__file__).parent
ENTRADA = CARPETA / "contactos.txt"
SALIDA = CARPETA / "contactos_validos.txt"

PATRON_DNI = r"\d{7,8}"
PATRON_EMAIL = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"


class ContactoInvalidoError(Exception):
    """Se lanza cuando un contacto tiene datos con formato inválido."""
    pass


def validar_contacto(linea, numero_linea):
    partes = linea.split(";")
    if len(partes) != 3:
        raise ContactoInvalidoError(f"línea {numero_linea}: formato incorrecto, se esperaba nombre;dni;email")
    nombre, dni, email = (p.strip() for p in partes)
    if not re.fullmatch(PATRON_DNI, dni):
        raise ContactoInvalidoError(f"{nombre}: DNI inválido '{dni}' (debe tener 7 u 8 dígitos)")
    if not re.fullmatch(PATRON_EMAIL, email):
        raise ContactoInvalidoError(f"{nombre}: email inválido '{email}'")
    return nombre, dni, email


def crear_archivo_prueba():
    contactos = [
        "Ana Gómez;40123456;ana.gomez@gmail.com",
        "Bruno Díaz;123;bruno@hotmail.com",          # DNI inválido
        "Carla Ruiz;38999111;carla.ruiz@empresa",     # Email inválido 
        "Diego Pérez;7654321;diego.perez@uai.edu.ar",
        "Elena Sosa;35111222",                         # Formato incorrecto
        "Federico Paz;41A22333;fede@gmail.com",        # DNI con letra
    ]
    with open(ENTRADA, "w", encoding="utf-8") as f:
        f.write("\n".join(contactos) + "\n")


def procesar_contactos():
    validos = []
    with open(ENTRADA, "r", encoding="utf-8") as f:
        for i, linea in enumerate(f, start=1):
            linea = linea.strip()
            if not linea:
                continue
            try:
                validos.append(validar_contacto(linea, i))
            except ContactoInvalidoError as e:
                print(f"Descartado -> {e}")

    with open(SALIDA, "w", encoding="utf-8") as f:
        for nombre, dni, email in validos:
            f.write(f"{nombre};{dni};{email}\n")
    return validos


if __name__ == "__main__":
    crear_archivo_prueba()
    print(f"Leyendo {ENTRADA.name}...\n")
    validos = procesar_contactos()

    print(f"\nContactos válidos: {len(validos)}. Contenido de {SALIDA.name}:")
    with open(SALIDA, "r", encoding="utf-8") as f:
        print(f.read(), end="")
