class Persona:
    def __init__(self , nombre , apellido ,  rut):
        self.nombre = nombre
        self.apellido = apellido
        self.rut = rut
    def __str__(self):
        # return f'{self.nombre} {self.apellido} {self.rut}'
        return self

class Cliente(Persona):
    def __init__(self ,  identificador , nombre , apellido , rut):
        super().__init__(nombre , apellido , rut)
        self.identificador = identificador
        self.cuenta = Cuenta()
        # super(Cuenta).__init__(self.saldo , self.interes , self.saldoConInteres)

class Cuenta:
    def __init__(self):
        # self.tipo = corriente o jubilacion , vivienda , etc
        self.saldo = 100
        self.interes = 10
        self.saldoConInteres = 110

    def deposito(self):
        return f'esto es un deposito'

    def retiro(self):
        return f'esto es un retiro'

    def transferencia(self):
        return f'esto es una transferencia'
    
    def verSaldo(self):
        # return f'esto es el saldo'
        return f'el saldo es: {self.saldo} , el interes es: {self.interes} y el total es: {self.saldoConInteres}'
    
    def __str__(self):
        return f'{self.saldo} {self.interes} {self.saldoConInteres}'

# class CuentaTipo(cuenta)  Continuar desde aqui , explicacion linea 19

class Usuario(Cliente):
    def __init__(self , nickName , clave , email ,identificador , nombre , apellido , rut):
        super().__init__(identificador, nombre , apellido , rut)
        self.nickName = nickName
        self.clave = clave
        self.email = email

    def __str__(self):
        return f'{self.nickName} {self.clave} {self.email} {self.identificador} {self.nombre} {self.apellido} {self.rut} '

usuario1 = Usuario('gorylactics' , 123 , 'adrian@adrian.pl' , 'Id = 1' ,  'Adrian' , 'Miranda' , '15844444-4' , )
print(usuario1)
print(usuario1.cuenta.verSaldo())
usuario1.clave = 456
print(usuario1)



