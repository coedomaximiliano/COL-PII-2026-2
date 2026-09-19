#Definí una clase Estudiante con un atributo de instancia nombre.
#Agregále un atributo de CLASE que cuente cuántos estudiantes se crearon en total, y actualizalo en el constructor.
#Agregá un @classmethod llamado total_estudiantes() que devuelva ese contador.
#Tu programa debe:
#Crear al menos tres estudiantes.
#Mostrar el total de estudiantes creados usando el classmethod.

class Estudiante:
    total_estudiantes = 0

    def __init__(self, nombre):
        self.nombre = nombre
        Estudiante.total_estudiantes += 1

    @classmethod
    def get_total_estudiantes(cls):
        return cls.total_estudiantes 

estudiante1 = Estudiante("Ana")
estudiante2 = Estudiante("Pedro")
estudiante3 = Estudiante("Lucia")
print("Estudiante:", estudiante1.nombre)
print("Estudiante:", estudiante2.nombre)
print("Estudiante:", estudiante3.nombre)
print("Total de estudiantes:", Estudiante.get_total_estudiantes())