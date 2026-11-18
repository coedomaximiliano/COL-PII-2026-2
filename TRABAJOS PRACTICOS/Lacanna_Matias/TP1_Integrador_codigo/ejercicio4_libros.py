# Ejercicio 4 

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
            print(f"Se prestó '{self.titulo}'")
        else:
            print(f"'{self.titulo}' ya está prestado")

    def devolver(self):
        if not self.__disponible:
            self.__disponible = True
            print(f"Se devolvió '{self.titulo}'")
        else:
            print(f"'{self.titulo}' no estaba prestado")


class LibroLibreria(Libro):
    
    def __init__(self, titulo, autor, precio, stock):
        super().__init__(titulo, autor)
        self.precio = precio
        self.__stock = stock

    @property
    def stock(self):
        return self.__stock

    def vender(self, cantidad):
        if cantidad > self.__stock:
            print(f"Stock insuficiente de '{self.titulo}': hay {self.__stock}")
        else:
            self.__stock -= cantidad
            print(f"Vendidas {cantidad} unidades de '{self.titulo}' por ${cantidad * self.precio:,.2f}")


if __name__ == "__main__":
    lb = LibroBiblioteca("Rayuela", "Julio Cortázar")
    ll = LibroLibreria("Ficciones", "Jorge Luis Borges", precio=25000, stock=5)

    print("Disponible:", lb.disponible)
    lb.prestar()
    print("Disponible:", lb.disponible)
    lb.prestar()         
    lb.devolver()
    print("Disponible:", lb.disponible)

    print("Stock:", ll.stock)
    ll.vender(3)
    print("Stock:", ll.stock)
    ll.vender(10)     

    print("Total de libros creados:", Libro.total_libros)
