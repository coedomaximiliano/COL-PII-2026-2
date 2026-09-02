"""
SOLUCIÓN — Ejercicio 3 · Integrador · Sistema de reservas
(Diapositiva "EJERCICIO 3 · INTEGRADOR" de la Clase 4)

Consigna: Diseñá una clase Reserva que combine variable de instancia y de
clase, un atributo privado (encapsulamiento) y un método de clase para
contar reservas.

Integra los 4 temas de la clase:
- Variables de instancia: cliente, monto, __confirmada (propias de c/objeto)
- Variable de clase: total_reservas (compartida por todas las reservas)
- Constructor y destructor: __init__ y __del__
- Encapsulamiento: __confirmada es privada, se expone de solo lectura con
  @property y solo se modifica a través de confirmar()
"""


class Reserva:
    total_reservas = 0  # variable de clase

    def __init__(self, cliente, monto):
        self.cliente = cliente
        self.monto = monto
        self.__confirmada = False  # atributo privado (encapsulamiento)
        Reserva.total_reservas += 1
        print(f"Reserva creada para {self.cliente} (${self.monto})")

    @classmethod
    def contador(cls):
        """Método de clase: devuelve cuántas reservas existen en total."""
        return cls.total_reservas

    @property
    def confirmada(self):
        """Solo lectura: desde afuera no se puede hacer reserva.confirmada = True"""
        return self.__confirmada

    def confirmar(self):
        self.__confirmada = True
        print(f"Reserva de {self.cliente} confirmada")

    def __del__(self):
        print(f"Se canceló/eliminó la reserva de {self.cliente}")


if __name__ == "__main__":
    r1 = Reserva("Camila", 15000)
    r2 = Reserva("Bruno", 22000)

    r1.confirmar()
    print(f"¿{r1.cliente} confirmada? {r1.confirmada}")
    print(f"¿{r2.cliente} confirmada? {r2.confirmada}")

    print(f"Total de reservas creadas: {Reserva.contador()}")

    del r2  # dispara __del__
