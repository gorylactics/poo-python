class CuentaBancaria:
    def __init__(self):
        self.cuenta = 0
        self.interes = float(0.01)
        self.totalInteres = 0
        self.totalCuenta = 0
    
    def deposito(self , deposito):
        self.cuenta += deposito
        return self
    
    def retiro(self , montoRetiro):
        if self.cuenta > montoRetiro:
            self.cuenta -= montoRetiro
        else:
            print(f'no hay saldo suficiente, su saldo es: {self.cuenta}')
        return self
    
    def mostrarSaldo(self):
        return print(f'Su saldo es: {self.cuenta}')
        
    def saldoConInteres(self):
        if self.cuenta > 0:
            self.totalInteres = (self.cuenta * self.interes)
            self.totalCuenta = self.cuenta + self.totalInteres
        else:
            print('no hay saldo')
        return self

    def __str__(self):
        return f'Sin interes la cuenta posee: {self.cuenta} , con interes tiene: {self.totalCuenta}'

cuenta1 = CuentaBancaria()
cuenta1.deposito(3000).deposito(4500).deposito(100).retiro(7000)
cuenta1.saldoConInteres()
print(cuenta1)

cuenta2 = CuentaBancaria()
cuenta2.deposito(1000).deposito(1000).retiro(200).retiro(200).retiro(200).retiro(200)
cuenta2.saldoConInteres()
print(cuenta2)
