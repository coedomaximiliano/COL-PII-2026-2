# Ejercicio 3 


class CuentaBancaria:
    def __init__(self):
        self.saldo = 0

    def depositar(self, monto):
        if monto <= 0:
            print("Error: el monto a depositar debe ser positivo")
            return
        self.saldo += monto
        print(f"Depósito de ${monto}. Saldo: ${self.saldo}")

    def retirar(self, monto):
        if monto <= 0:
            print("Error: el monto a retirar debe ser positivo")
        elif monto > self.saldo:
            print(f"Error: saldo insuficiente para retirar ${monto} (saldo: ${self.saldo})")
        else:
            self.saldo -= monto
            print(f"Retiro de ${monto}. Saldo: ${self.saldo}")


if __name__ == "__main__":
    cuenta = CuentaBancaria()
    cuenta.depositar(1000)
    cuenta.retirar(300)   
    cuenta.retirar(5000)  
    print("Saldo final:", cuenta.saldo)
