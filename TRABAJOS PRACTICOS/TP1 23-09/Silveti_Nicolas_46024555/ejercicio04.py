class Libro:
    total_libros = 0

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        Libro.total_libros += 1


class LibroBiblioteca(Libro):
    def __init__(self, titulo, autor):
        super().__init__(titulo, autor)
        self.__disponible = True

    @property
    def disponible(self):
        return self.__disponible

    def prestar(self):
        if self.__disponible:
            self.__disponible = False
            print(f"Se prestó el libro '{self.titulo}'.")
        else:
            print(f"El libro '{self.titulo}' ya está prestado.")

    def devolver(self):
        if not self.__disponible:
            self.__disponible = True
            print(f"Se devolvió el libro '{self.titulo}'.")
        else:
            print(f"El libro '{self.titulo}' ya está disponible.")


class LibroLibreria(Libro):
    def __init__(self, titulo, autor, precio, stock):
        super().__init__(titulo, autor)
        self.precio = precio
        self.__stock = stock

    @property
    def stock(self):
        return self.__stock

    def vender(self, unidades):
        if unidades <= 0:
            print("Las unidades deben ser mayores que cero.")
        elif unidades > self.__stock:
            print(f"No hay suficientes ejemplares de '{self.titulo}'.")
        else:
            self.__stock -= unidades
            print(f"Se vendieron {unidades} ejemplares de '{self.titulo}'.")


ejemplar_prestamo = LibroBiblioteca(
    "Fahrenheit 451",
    "Ray Bradbury"
)

ejemplar_venta = LibroLibreria(
    "El hobbit",
    "J. R. R. Tolkien",
    22000,
    12
)

# Consultar disponibilidad, prestar y devolver
print(f"Libro: {ejemplar_prestamo.titulo}")
print(f"Disponible al inicio: {ejemplar_prestamo.disponible}")

ejemplar_prestamo.prestar()
print(f"Disponible después del préstamo: {ejemplar_prestamo.disponible}")

ejemplar_prestamo.devolver()
print(f"Disponible después de devolver: {ejemplar_prestamo.disponible}")

# Consultar stock y probar ventas
print(f"\nLibro: {ejemplar_venta.titulo}")
print(f"Precio: ${ejemplar_venta.precio}")
print(f"Stock inicial: {ejemplar_venta.stock}")

ejemplar_venta.vender(4)
print(f"Stock después de vender: {ejemplar_venta.stock}")

ejemplar_venta.vender(10)
print(f"Stock final: {ejemplar_venta.stock}")

print(f"\nTotal de libros creados: {Libro.total_libros}")