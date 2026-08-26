"""
EJERCICIO 2 · INDIVIDUAL — Practicar la abstracción
Consigna: para cada entidad, indicar dos atributos y un método que le
agregarías si tuvieras que representarla como clase en un sistema de
biblioteca.

Esto es un ejercicio de ABSTRACCIÓN: no hay una única respuesta correcta,
lo importante es justificar qué es relevante para ESTE sistema puntual
(una biblioteca) y qué se descarta. Para que quede más concreto, acá se
modela cada entidad como una clase real, con comentarios explicando el
criterio de selección.
"""


# a) Un libro
# Relevante para una biblioteca: identificar el libro y saber si se puede
# prestar. NO nos importa, por ejemplo, el color de tapa o el editor.
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True  # estado que cambia con cada préstamo

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f'"{self.titulo}" fue prestado')
        else:
            print(f'"{self.titulo}" no está disponible')


# b) Un socio de la biblioteca
# Relevante: identificarlo y saber cuántos libros tiene en préstamo.
# NO nos importa, por ejemplo, su dirección o su teléfono para este caso.
class Socio:
    def __init__(self, nombre, numero_socio):
        self.nombre = nombre
        self.numero_socio = numero_socio
        self.libros_prestados = []

    def retirar_libro(self, libro):
        libro.prestar()
        self.libros_prestados.append(libro)


# c) Un préstamo de libro
# Relevante: qué libro, a quién y desde cuándo. NO nos importa, por
# ejemplo, en qué sucursal física se hizo el trámite.
class Prestamo:
    def __init__(self, libro, socio, fecha_inicio):
        self.libro = libro
        self.socio = socio
        self.fecha_inicio = fecha_inicio

    def resumen(self):
        print(f"{self.socio.nombre} retiró '{self.libro.titulo}' el {self.fecha_inicio}")


# --- Ejemplo de uso ---
libro1 = Libro("Cien años de soledad", "García Márquez")
socio1 = Socio("Sofía", numero_socio=101)
socio1.retirar_libro(libro1)

prestamo1 = Prestamo(libro1, socio1, "2026-08-26")
prestamo1.resumen()
