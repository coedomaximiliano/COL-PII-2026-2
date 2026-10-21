"""
EJEMPLO — Destructores
El destructor __del__ se ejecuta cuando el objeto va a eliminarse de
memoria, generalmente porque ya no queda ninguna referencia hacia él.
Se usa poco, sobre todo para liberar recursos.
"""


class ConexionSimulada:
    def __init__(self, servidor):
        self.servidor = servidor
        print(f"[CONSTRUCTOR] Conectando a {self.servidor}")

    def __del__(self):
        print(f"[DESTRUCTOR] Cerrando la conexión a {self.servidor}")


conexion = ConexionSimulada("db.escuela.edu")
print("Usando la conexión...")
del conexion  # dispara __del__ de forma explícita
