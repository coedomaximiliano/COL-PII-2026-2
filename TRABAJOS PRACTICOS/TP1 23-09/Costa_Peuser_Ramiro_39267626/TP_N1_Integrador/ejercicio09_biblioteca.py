#Biblioteca (composición + excepciones propias)
#Definí una clase Libro con atributos titulo y disponible (arranca en True).
#Definí una clase Biblioteca que mantenga una lista de libros, con métodos prestar(titulo) y devolver(titulo).
#Definí tu propia excepción LibroNoDisponibleError. prestar() debe lanzarla si el libro no existe o ya está prestado.
#Tu programa debe:
#Cargar al menos dos libros en la biblioteca.
#Prestar un libro, y luego intentar prestarlo de nuevo capturando la excepción con try/except para mostrar un mensaje amigable (sin que el programa se corte).
#Devolver el libro y volver a prestarlo para confirmar que funciona.

class Libro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.disponible = True

class LibroNoDisponibleError(Exception):
    pass

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def prestar(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                if libro.disponible:
                    libro.disponible = False
                    print(f"El libro '{titulo}' ha sido prestado.")
                    return
                else:
                    raise LibroNoDisponibleError("El libro no está disponible")
        raise LibroNoDisponibleError("El libro no existe")

    def devolver(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                if not libro.disponible:
                    libro.disponible = True
                    print(f"El libro '{titulo}' ha sido devuelto.")
                    return
                else:
                    raise LibroNoDisponibleError("El libro ya estaba disponible")
        raise LibroNoDisponibleError("El libro no existe")

biblioteca = Biblioteca()
libro1 = Libro("El Principito")
libro2 = Libro("1984")
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

#Prueba positiva: prestar y devolver un libro

biblioteca.prestar("El Principito")
biblioteca.devolver("El Principito")

#Prueba negativa: intentar prestar un libro que ya está prestado y devolver un libro que ya está disponible

biblioteca.prestar("1984")
try:
    biblioteca.prestar("1984")
except LibroNoDisponibleError as e:
    print(e)

biblioteca.devolver("1984")
try:
    biblioteca.devolver("1984")
except LibroNoDisponibleError as e:
    print(e)