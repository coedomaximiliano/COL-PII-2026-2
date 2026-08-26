"""
EJERCICIO 9 (Difícil) — Composición + excepciones propias: Biblioteca
Consigna: clase Libro (titulo, disponible=True). Clase Biblioteca con una
lista de libros y métodos prestar(titulo) / devolver(titulo). Si se intenta
prestar un libro que no existe o que no está disponible, debe lanzarse una
excepción propia LibroNoDisponibleError, capturada al usar la biblioteca
para mostrar un mensaje amigable en vez de romper el programa.
"""


class LibroNoDisponibleError(Exception):
    """Excepción propia: se lanza si el libro no existe o ya está prestado."""
    pass


class Libro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.disponible = True


class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def _buscar(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                return libro
        return None

    def prestar(self, titulo):
        libro = self._buscar(titulo)
        if libro is None or not libro.disponible:
            raise LibroNoDisponibleError(f'"{titulo}" no está disponible para préstamo')
        libro.disponible = False
        print(f'Te llevaste "{titulo}"')

    def devolver(self, titulo):
        libro = self._buscar(titulo)
        if libro is not None:
            libro.disponible = True
            print(f'Devolviste "{titulo}"')


biblio = Biblioteca()
biblio.agregar_libro(Libro("Cien años de soledad"))
biblio.agregar_libro(Libro("Rayuela"))

biblio.prestar("Rayuela")

# Intentamos prestar el mismo libro de nuevo: debe fallar de forma controlada
try:
    biblio.prestar("Rayuela")
except LibroNoDisponibleError as error:
    print(f"No se pudo completar el préstamo: {error}")

# Intentamos prestar un libro que no existe
try:
    biblio.prestar("Ficciones")
except LibroNoDisponibleError as error:
    print(f"No se pudo completar el préstamo: {error}")

biblio.devolver("Rayuela")
biblio.prestar("Rayuela")  # ahora sí funciona
