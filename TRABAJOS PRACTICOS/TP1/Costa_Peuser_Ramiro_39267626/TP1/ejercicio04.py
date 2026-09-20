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
            print(f"'{self.titulo}' fue prestado.")
        else:
            print(f"'{self.titulo}' no está disponible.")

    def devolver(self):
        if not self.__disponible:
            self.__disponible = True
            print(f"'{self.titulo}' fue devuelto.")
        else:
            print(f"'{self.titulo}' ya estaba disponible.")


class LibroLibreria(Libro):
    def __init__(self, titulo, autor, precio, stock):
        super().__init__(titulo, autor)
        self.precio = precio
        self.__stock = stock

    @property
    def stock(self):
        return self.__stock

    def vender(self, cantidad):
        if cantidad <= 0:
            print("La cantidad debe ser mayor que 0.")
        elif cantidad <= self.__stock:
            self.__stock -= cantidad
            print(f"Se vendieron {cantidad} unidades de '{self.titulo}'.")
        else:
            print(f"No hay suficiente stock de '{self.titulo}'.")


# Crear libros
libro_biblioteca = LibroBiblioteca(
    "El Principito",
    "Antoine de Saint-Exupéry"
)

libro_libreria = LibroLibreria(
    "1984",
    "George Orwell",
    15000,
    10
)


# LIBRO DE BIBLIOTECA

print("Estado inicial:", libro_biblioteca.disponible)

libro_biblioteca.prestar()
print("Después de prestar:", libro_biblioteca.disponible)

libro_biblioteca.devolver()
print("Después de devolver:", libro_biblioteca.disponible)


# LIBRO DE LIBRERÍA

print("\nStock inicial:", libro_libreria.stock)
print("Intentar vender 3 unidades:")
libro_libreria.vender(3)
print("Stock después de vender:", libro_libreria.stock)
print("Intentar vender 10 unidades:")
libro_libreria.vender(10)
print("Stock final:", libro_libreria.stock)


# TOTAL DE LIBROS

print("\nTotal de libros creados:", Libro.total_libros)