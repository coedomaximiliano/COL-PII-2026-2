"""
EJEMPLO — Variables de clase
Son atributos compartidos por TODOS los objetos de una clase. Se declaran
en el cuerpo de la clase (fuera de __init__) y su valor es común a todas
las instancias, salvo que una instancia lo pise puntualmente.
"""


class Empleado:
    empresa = "Tech Solutions SA"  # variable de clase, común a todos
    cantidad_empleados = 0

    def __init__(self, nombre):
        self.nombre = nombre  # variable de instancia
        Empleado.cantidad_empleados += 1

    def mostrar(self):
        print(f"{self.nombre} trabaja en {Empleado.empresa}")


e1 = Empleado("Marina")
e2 = Empleado("Diego")

e1.mostrar()
e2.mostrar()

print(f"Cantidad de empleados creados: {Empleado.cantidad_empleados}")

# Si cambia la variable de clase, afecta a todas las instancias
Empleado.empresa = "Tech Solutions SA (nueva sede)"
e1.mostrar()
e2.mostrar()
