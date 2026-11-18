# Ejercicio 2 


class EdadInvalidaError(Exception):
    pass


class Persona:
    def __init__(self, nombre, edad):
        if edad < 0:
            raise EdadInvalidaError(f"La edad de {nombre} no puede ser negativa ({edad})")
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"{self.nombre}, {self.edad} años"


if __name__ == "__main__":
    p1 = Persona("Matías", 25)
    print("Persona creada:", p1)

    try:
        p2 = Persona("Juan", -3)
    except EdadInvalidaError as e:
        print("No se pudo crear la persona:", e)

    print("El programa sigue funcionando")
