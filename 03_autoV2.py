class Auto:
    def __init__(self ,  marca , modelo):
        self.marca = marca
        self.modelo = modelo
        self.encendido = False

    def arranque(self , encendido):
        pass

    def __str__(self):
        return(f"Marca: {self.marca}\nModelo: {self.modelo}")

auto1 = Auto("subaru" , "legacy")
print(auto1)