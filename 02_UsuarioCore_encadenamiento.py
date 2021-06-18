class Usuario:
    def __init__(self , nombre , email):
        self.nombre = nombre
        self.email = email
        self.cuenta = 0

    def deposito(self , deposito):
        self.cuenta += deposito
        return self
    
    def retiro(self , retiro):
        if retiro < self.cuenta:
            self.cuenta -= retiro
            print(f"el retiro ha sido de: {retiro} y ha quedado con un saldo de: {self.cuenta}")
        else:
            print( f"No tiene saldo suficiente, su saldo es: {self.cuenta} ")
        return self
    
    def mostrarSaldo(self):
        return print(f"Su Saldo es de: {self.cuenta}")

    def transferencia(self , traspaso , destino):
        if self.cuenta > traspaso:
            self.cuenta -= traspaso
            destino.cuenta += traspaso
            print(f"Ha realizado una transferencia a: {destino.nombre} por un monto de {traspaso} , su saldo actual es: {self.cuenta}")
        else:
            return print('saldo insuficiente')
        return self
    
    
    def __str__(self):
        return f"Nombre: {self.nombre}\nEmail: {self.email}\nCuenta: {self.cuenta}\n"

user1 = Usuario('adrian' , 'adrian@email.pl')
user1.deposito(1000).deposito(1000).deposito(1000).deposito(100).retiro(100).retiro(600)
print(user1)

user2 = Usuario('rodrigo' , 'rodrigo@rodrigo.pl')
user2.deposito(1000).deposito(3000).retiro(500).retiro(100)
print(user2)

user3 = Usuario('gory' , 'gory@gory.pl')
user3.deposito(500).retiro(100)
print(user3)

user1.transferencia(100 , user3)
print(user1)
