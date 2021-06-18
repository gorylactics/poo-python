class CuentaBancaria:
    def __init__(self):
        self.cuenta = 0
        self.interes = self.cuenta * float(0.01)
        self.totalCuenta = self.cuenta + self.interes
    
    def __str__(self):
        return f'La cuenta posee: {self.cuenta}, ha generado un interes de: {self.interes}, el total acumulado es: {self.totalCuenta}'

cuenta1 = CuentaBancaria()
cuenta1.cuenta = 1000
print(cuenta1)
