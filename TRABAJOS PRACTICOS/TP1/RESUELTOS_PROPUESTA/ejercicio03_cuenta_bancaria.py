"""
EJERCICIO 3 (Fácil) — Clase CuentaBancaria
Consigna: definir una clase CuentaBancaria con atributo saldo (arranca en 0).
Métodos depositar(monto) y retirar(monto); retirar debe validar que no se
saque más saldo del disponible, mostrando un mensaje de error en ese caso
en vez de romper el programa.
"""


class CuentaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0

    def depositar(self, monto):
        self.saldo += monto
        print(f"Depositaste ${monto}. Saldo actual: ${self.saldo}")

    def retirar(self, monto):
        if monto > self.saldo:
            print(f"No se puede retirar ${monto}: el saldo disponible es ${self.saldo}")
        else:
            self.saldo -= monto
            print(f"Retiraste ${monto}. Saldo actual: ${self.saldo}")


cuenta = CuentaBancaria("Sofía")
cuenta.depositar(1000)
cuenta.retirar(300)
cuenta.retirar(5000)  # debe mostrar el error, sin romper el programa
print(f"Saldo final: ${cuenta.saldo}")
