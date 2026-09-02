"""
SOLUCIÓN — Ejercicio 1 · Cuenta bancaria con condicionales
(Diapositiva "EJERCICIO 1 · INDIVIDUAL" de la Clase 4)

Consigna: Implementá una clase CuentaBancaria con saldo como variable de
instancia y métodos depositar() y retirar() que usen condicionales para
validar montos.
"""


class CuentaBancaria:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def depositar(self, monto):
        if monto <= 0:
            print("El monto a depositar debe ser mayor a 0")
            return
        self.saldo += monto
        print(f"Depositaste ${monto}. Nuevo saldo: ${self.saldo}")

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            print(f"Retiraste ${monto}. Nuevo saldo: ${self.saldo}")
        else:
            print(f"Saldo insuficiente: tenés ${self.saldo} y querés retirar ${monto}")


if __name__ == "__main__":
    cuenta = CuentaBancaria(1000)
    cuenta.depositar(500)     # saldo: 1500
    cuenta.retirar(2000)      # saldo insuficiente, no se modifica
    cuenta.retirar(300)       # saldo: 1200
