#Cuenta bancaria
#Definí una clase CuentaBancaria con un atributo saldo, que arranca en 0.
#Agregále los métodos depositar(monto) y retirar(monto).
#Tu programa debe:
#retirar() no debe permitir sacar más saldo del disponible: si el monto pedido es mayor al saldo, mostrar un mensaje de error en vez de dejar el saldo en negativo.
#Probar la clase depositando, retirando un monto válido, y luego intentando retirar un monto mayor al saldo disponible.


class CuentaBancaria:
    def __init__(self):
        self.saldo = 0

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Depósito exitoso: ${monto}. Saldo actual: ${self.saldo}.")
        else:
            print("Error:El monto a depositar debe ser mayor a 0.")

    def retirar(self, monto):
        if monto > self.saldo:
            print("Error: No se puede retirar más del saldo disponible.")
        elif monto <= 0:
            print("El monto a retirar debe ser mayor a 0.")
        else:
            self.saldo -= monto
            print(f"Retiro exitoso: ${monto}. Saldo actual: ${self.saldo}.")

# Probar la clase
cuenta = CuentaBancaria()
cuenta.depositar(1000)  # Depositar un monto válido
cuenta.depositar(-100)  # Intentar depositar un monto negativo
cuenta.retirar(500)    # Retirar un monto válido
cuenta.retirar(600)    # Intentar retirar un monto mayor al saldo disponible