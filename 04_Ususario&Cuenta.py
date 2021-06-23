class Usuario:
    
    def __init__(self , nombre , email):
        self.nombre = nombre
        self.email = email
        self.cuentas = []

    def agregarCuentas(self ,  cuentaNueva):
        self.cuentas.append(cuentaNueva)
        return self
    
    def mostrarSaldo(self , cuenta):
        return print(f'Su saldo es: {self.cuentas}')
    
    def mostrarCuentas(self , cuentas):
        for cuenta in cuentas:
            print(cuenta)

    # def transferencia(self , cuentaOrigen , traspaso  , destino):
    #     if self.cuentaOrigen > traspaso:
    #         self.cuentaOrigen -= traspaso
    #         destino.cuentaOrigen += traspaso
    #         # print(f"Ha realizado una transferencia a: {destino.nombre} por un monto de {traspaso} , su saldo actual es: {self.cuenta}")
    #     else:
    #         return print('saldo insuficiente')
    #     return self
    
    def __str__(self):
        return f"Nombre: {self.nombre}\nEmail: {self.email}\nCuenta: {self.cuentas}\n"

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
        if self.cuentaS > 0:
            self.totalInteres = (self.cuentaS * self.interes)
            self.totalCuenta = self.cuentaS + self.totalInteres
        else:
            print('no hay saldo')
        return self

    def __str__(self):
        return f'Sin interes la cuenta posee: {self.cuenta} , con interes tiene: {self.totalCuenta}'

gosia = Usuario('gosia' , 'gosiaDeAdrian@unaMillaMenos.pl')
cuenta1 = CuentaBancaria()
cuenta2 = CuentaBancaria()
gosia.agregarCuentas(cuenta1)
gosia.agregarCuentas(cuenta2)
print(gosia)
