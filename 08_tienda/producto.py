class Producto:
    def __init__(self, nombre , precio , categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
    
    def actualizarPrecio(self , impuesto , incrementado):
        if incrementado == True:
            self.precio += (self.precio * impuesto)
        else:
            self.precio -= (self.precio * impuesto)
    def impresion(self):
        return f'Producto: {self.nombre}\nCategoria: {self.categoria}\nPrecio: {self.precio}'

if __name__ == '__main__':
    platano = Producto('Platano', 100 , 'Frutas')
    print(platano.impresion())
    platano.actualizarPrecio(0.20 , True)
    print(platano.precio)
    platano.actualizarPrecio(0.20 , False)
    print(platano.precio)

# print(locals())