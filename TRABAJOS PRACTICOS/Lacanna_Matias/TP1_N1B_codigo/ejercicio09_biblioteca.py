# Ejercicio 9 


class LibroNoDisponibleError(Exception):
    """Se lanza cuando un libro no existe o ya está prestado."""
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
        if libro is None:
            raise LibroNoDisponibleError(f"El libro '{titulo}' no existe en la biblioteca")
        if not libro.disponible:
            raise LibroNoDisponibleError(f"El libro '{titulo}' ya está prestado")
        libro.disponible = False
        print(f"Se prestó '{titulo}'")

    def devolver(self, titulo):
        libro = self._buscar(titulo)
        if libro is not None and not libro.disponible:
            libro.disponible = True
            print(f"Se devolvió '{titulo}'")
        else:
            print(f"No se puede devolver '{titulo}': no existe o no estaba prestado")


def intentar_prestar(biblioteca, titulo):
    try:
        biblioteca.prestar(titulo)
    except LibroNoDisponibleError as e:
        print("Aviso:", e)


if __name__ == "__main__":
    b = Biblioteca()
    b.agregar_libro(Libro("El Aleph"))
    b.agregar_libro(Libro("Martín Fierro"))

    intentar_prestar(b, "El Aleph")       
    intentar_prestar(b, "El Aleph")      
    intentar_prestar(b, "Don Quijote")   
    b.devolver("El Aleph")
    intentar_prestar(b, "El Aleph")    
    print("El programa terminó sin cortarse")
