"""
EJEMPLO — Constructores y destructores
El constructor (__init__) se ejecuta automáticamente al crear un objeto
con Clase(...) e inicializa sus atributos. El destructor (__del__) se
ejecuta cuando el objeto es eliminado (por del o por quedar sin
referencias), útil para liberar recursos.
"""


class ArchivoLog:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lineas = []
        print(f"[CONSTRUCTOR] Se abrió el archivo de log '{self.nombre}'")

    def escribir(self, mensaje):
        self.lineas.append(mensaje)
        print(f"LOG ({self.nombre}): {mensaje}")

    def __del__(self):
        print(f"[DESTRUCTOR] Cerrando '{self.nombre}' "
              f"({len(self.lineas)} líneas escritas)")


log = ArchivoLog("sistema.log")
log.escribir("Inicio del programa")
log.escribir("Proceso completado con éxito")

del log  # dispara __del__ explícitamente
