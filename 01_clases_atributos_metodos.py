class primeraClase:
    def __init__(self):
        super().__init__()

class segundaClase:
    def __init__(self):
        self.nombre = 'adrian'
        self.apellido = 'miranda'
        self.idUser = 1

user = segundaClase()
print(f'el usuario es: {user.nombre} {user.apellido} y su id es: {user.idUser}')

class terceraClase:
    def __init__(self , nombre , apellido , rut):
        self.nombre = nombre
        self.apellido = apellido
        self.rut = rut
        self.saldo = 0
    def deposito(self , ingreso):
        self.saldo += ingreso

usuario = terceraClase('adrian' , 'miranda' , 15000000-0)
# print(usuario.nombre)
# print(usuario.apellido)
# print(usuario.rut)
print(usuario.saldo)
usuario.deposito(100)
print(usuario.saldo)

