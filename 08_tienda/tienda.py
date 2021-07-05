from producto import Producto

class Tienda:
    def __init__(self , nombre):
        self.nombre = nombre
        self.listaProductos = []
    
    def agregarProducto(self , producto):
        self.listaProductos.append({producto})
    
    def venderProducto(self , producto):
        for producto in self.listaProductos:
            self.listaProductos.remove(producto)

    # def inflacion(self ,  categoria , actualizarPrecio):
    #     self.categoria = Producto
    #     self.actualizarPrecio = Producto.actualizarPrecio()

    # def inflacion(self ,  categoria , actualizarPrecio):
    #     self.categoria = self.listaProductos[Producto.categoria]
    #     self.actualizarPrecio = self.listaProductos[Producto.actualizarPrecio]

if __name__ == '__main__':
    
    goryStore = Tienda('goryStore')
    platano2 = Producto('platano2',150,'frutas')
    goryStore.agregarProducto(platano2.impresion())
    print(goryStore.listaProductos)
    goryStore.venderProducto(platano2)
    print(goryStore.listaProductos)

    platano3 = Producto('platano3' , 150 , 'frutas')
    
    platano3.actualizarPrecio(0.25 , True)
    goryStore.agregarProducto(platano3.impresion())
    print(goryStore.listaProductos)

    platano4 = Producto('platano4' , 150 , 'frutas')
    goryStore.agregarProducto(platano4.impresion())
    print(goryStore.listaProductos)

    # goryStore.inflacion('frutas' , 0.20 , True)
    # print(goryStore.listaProductos)
    # Usar para el metodo inflacion
else:
    print('imprmiendo de manera global')