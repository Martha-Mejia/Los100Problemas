class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito de {cantidad} realizado. Saldo actual: {self.saldo}")
        else:
            print("La cantidad a depositar debe ser positiva.")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retiro de {cantidad} realizado. Saldo actual: {self.saldo}")
        elif cantidad > self.saldo:
            print("Fondos insuficientes para realizar el retiro.")
        else:
            print("La cantidad a retirar debe ser positiva.")

    def mostrar_saldo(self):
        print(f"Saldo actual: {self.saldo}")

# Ejemplo de uso:
cuenta = CuentaBancaria("Jorge el Curioso", 1000)

cuenta.mostrar_saldo()
cuenta.depositar(500)
cuenta.retirar(200)
cuenta.retirar(1500)
cuenta.mostrar_saldo()
