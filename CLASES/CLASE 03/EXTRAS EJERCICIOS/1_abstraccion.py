"""
EJERCICIOS — ABSTRACCIÓN
Recordá: abstraer es decidir qué atributos y comportamientos de una entidad
real son relevantes para EL PROBLEMA que queremos resolver, dejando de lado
todo lo demás.
"""

# ============================================================
# Ejercicio 1 (Fácil)
# Para un sistema de gestión académica, definí una clase Alumno que
# abstraiga SOLO lo que le importa a ese sistema: nombre, legajo y
# promedio. (Cosas como altura, color de pelo o gustos musicales no se
# modelan: no son relevantes para este problema).
# ============================================================


class Alumno:
    def __init__(self, nombre, legajo, promedio):
        self.nombre = nombre
        self.legajo = legajo
        self.promedio = promedio

    def resumen(self):
        print(f"Legajo {self.legajo} — {self.nombre} (promedio {self.promedio})")


a1 = Alumno("Sofía", 1023, 8.5)
a1.resumen()


# ============================================================
# Ejercicio 2 (Medio)
# Para un sistema de INVENTARIO de un kiosco, definí una clase Producto
# que abstraiga solo nombre, precio y stock. Agregá un método
# hay_stock() que devuelva True si el stock es mayor a 0.
# ============================================================


class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def hay_stock(self):
        return self.stock > 0


p1 = Producto("Alfajor", 800, 3)
p2 = Producto("Chicle", 300, 0)
print(f"{p1.nombre}: ¿hay stock? {p1.hay_stock()}")
print(f"{p2.nombre}: ¿hay stock? {p2.hay_stock()}")


# ============================================================
# Ejercicio 3 (Difícil)
# La MISMA entidad del mundo real —un Libro— se abstrae distinto según
# el sistema que la use. Definí dos clases Libro, una para una biblioteca
# (le importa si está disponible para préstamo) y otra para una librería
# de venta (le importa el precio y el stock). Mostrá que, aunque el
# objeto real es "el mismo libro", cada sistema modela cosas distintas.
# ============================================================


class LibroBiblioteca:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f'"{self.titulo}" prestado.')
        else:
            print(f'"{self.titulo}" no está disponible.')


class LibroLibreria:
    def __init__(self, titulo, precio, stock):
        self.titulo = titulo
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad=1):
        if cantidad <= self.stock:
            self.stock -= cantidad
            print(f'Vendidas {cantidad} unidades de "{self.titulo}". Quedan {self.stock}.')
        else:
            print(f'No hay stock suficiente de "{self.titulo}".')


libro_biblio = LibroBiblioteca("Rayuela", "Julio Cortázar")
libro_libreria = LibroLibreria("Rayuela", precio=15000, stock=5)

libro_biblio.prestar()
libro_libreria.vender(2)
