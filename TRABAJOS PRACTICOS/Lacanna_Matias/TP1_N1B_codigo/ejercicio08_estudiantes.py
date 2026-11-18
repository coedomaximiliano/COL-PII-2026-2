# Ejercicio 8 


class Estudiante:
    contador = 0 

    def __init__(self, nombre):
        self.nombre = nombre  
        Estudiante.contador += 1

    @classmethod
    def total_estudiantes(cls):
        return cls.contador


if __name__ == "__main__":
    e1 = Estudiante("Sofía")
    e2 = Estudiante("Tomás")
    e3 = Estudiante("Valentina")
    print("Estudiantes:", e1.nombre, e2.nombre, e3.nombre)
    print("Total de estudiantes creados:", Estudiante.total_estudiantes())
