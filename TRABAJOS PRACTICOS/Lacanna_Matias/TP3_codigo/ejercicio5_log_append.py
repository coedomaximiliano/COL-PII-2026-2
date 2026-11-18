# Ejercicio 5 

from datetime import datetime
from pathlib import Path

LOG = Path(__file__).parent / "operaciones.log"


def registrar_operacion(mensaje):
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] {mensaje}\n")


if __name__ == "__main__":
    LOG.unlink(missing_ok=True)  # Arrancamos con el log vacío para la prueba

    mensajes = ["Inicio de sesión del usuario mlacanna",
                "Se generó el reporte mensual",
                "Cierre de sesión"]
    for m in mensajes:
        registrar_operacion(m)

    with open(LOG, "r", encoding="utf-8") as f:
        lineas = f.readlines()

    print("Contenido del log:")
    print("".join(lineas), end="")
    presentes = all(any(m in l for l in lineas) for m in mensajes)
    print(f"\nLíneas en el archivo: {len(lineas)} | ¿Están las 3 operaciones?: {presentes}")
