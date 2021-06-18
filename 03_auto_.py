class Auto:
    def __init__(self , marca , modelo):
        self.marca = marca
        self.modelo = modelo
        self.encendido = False
        self.velocidad = 0

    def encendido(self):
        if self.encendido:
            print('el auto esta encendido')
            return self
        else:
            print('encienda el auto')
            return self
    
    def obtenerVelocidad(self):
        if self.encendido == False:
            print('el auto esta apagado')
        elif self.encendido == True and self.velocidad == 0:
            print('el auto esta detenido')
        elif self.encendido == True and self.velocidad > 0:
            print(f"la velocidad actual es de: {velocidad}")
            return self.velocidad
        return velocidad
    
    def __str__(self):
        return (f"Marca: {self.marca}\nModelo: {self.modelo}\nEncendido: {self.encendido}\nVelocidad: {self.velocidad}")

    # def ajustarVelocidad(self , velocidad):
        


# def AumentoSaldo(self , suma):
#         self.cuenta += suma
#         return self.cuenta


auto1 = Auto('subaru' , 'legacy')
# print(auto1.encendido)
# auto1.encendido = True
# print(auto1.encendido)
# print(auto1.velocidad)
auto1.encendido = True
print(auto1.encendido)




