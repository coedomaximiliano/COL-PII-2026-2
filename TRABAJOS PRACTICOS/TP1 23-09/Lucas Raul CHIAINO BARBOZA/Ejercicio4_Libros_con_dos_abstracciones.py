#Ejercicio 4: Libros con dos abstracciones

class Libro:
    total_libros = 0  # Variable de clase para contar el total de libros

    def __init__(self, titulo, autor):
        #Variables de instancia: se crean para cada libro
        self.titulo = titulo
        self.autor = autor

        #Aumento el contador cada vez que se crea un libro
        Libro.total_libros += 1

class LibroBiblioteca(Libro):
    def __init__(self, titulo, autor):
        super().__init__(titulo, autor)
        self.__disponible = True  # Atributo privado para indicar si el libro está disponible

    #Property de solo lectura
    @property
    def disponible(self):
        return self.__disponible

    def prestar(self):
        if self.__disponible:
            self.__disponible = False
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' no está disponible para préstamo.")

    def devolver(self):
        self.__disponible
        print(f"El libro '{self.titulo}' ha sido devuelto y está disponible nuevamente.")   


class LibroLibreria(Libro):
    def __init__(self, titulo, autor, precio, stock):
        super().__init__(titulo, autor)
        self.precio = precio
        self.__stock = stock

    #Property de solo lectura
    @property
    def stock(self):
        return self.__stock

    def vender(self, unidades):
        if unidades <= self.__stock:
            self.__stock -= unidades
            print(f"Se vendieron {unidades} unidades de '{self.titulo}'")
        else:
            print("No hay suficiente stock disponible")


# Creamos un libro para biblioteca y uno para libreria
libro_biblioteca = LibroBiblioteca(
    "Las haza{as del Capitan Tito}",
    "Tito Livio",
)

libro_libreria = LibroLibreria(
    "Cien anos de soledad",
    "Gabriel Garcia Marquez",
    25000,
    10
)


# Mostramos el estado inicial usando las properties
print(f"Disponible: {libro_biblioteca.disponible}")
print(f"Stock inicial: {libro_libreria.stock}")

print("-----------------------------")

# Prestamos y devolvemos el libro de biblioteca
libro_biblioteca.prestar()
print(f"Disponible despues del prestamo: {libro_biblioteca.disponible}")

libro_biblioteca.devolver()
print(f"Disponible despues de la devolucion: {libro_biblioteca.disponible}")

print("-----------------------------")

# Vendemos unidades del libro de libreria
libro_libreria.vender(3)
print(f"Stock despues de la venta: {libro_libreria.stock}")

print("-----------------------------")

# Mostramos el total de libros creados
print(f"Total de libros creados: {Libro.total_libros}")
