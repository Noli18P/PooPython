class Ropa():

    def __init__(self, color, talla, precio, nombre):
        self._color = color
        self._talla = talla
        self._precio = precio
        self._nombre = nombre
    
    def comprar(self, compra):
        if compra == 'si':
            return f'El producto {self._nombre} ha sido comprado'
        else:
            return f'El producto {self._nombre} no ha sido comprado'
    
    def informacion(self):
        print(f'El producto {self._nombre} tiene la siguiente informacion: ')
        print(f'Talla: {self._talla}')
        print(f'Color: {self._color}')
        print(f'Precio: {self._precio}')


class Sueter(Ropa):
    
    def __init__(self, color, talla, precio, nombre):
        super().__init__(color, talla, precio, nombre)


class Pantalon(Ropa):

    def __init__(self, color, talla, precio, nombre):
        super().__init__(color, talla, precio, nombre)


if __name__ == "__main__":
    comprar_producto = ''

    sueter = Sueter('rojo', 30, 15, 'sueter')
    sueter.informacion()
    
    comprar_producto = input('¿Deseas comprar el porducto? ').lower()
    if comprar_producto == 'si' or comprar_producto == 's':
        print(sueter.comprar(comprar_producto))
    else:
        print(sueter.comprar(comprar_producto))

    pantalon = Pantalon('azul', 32, 20, 'jeans')
    pantalon.informacion()

    comprar_producto = input('¿Deseas comprar el porducto? ').lower()
    if comprar_producto == 'si' or comprar_producto == 's':
        print(pantalon.comprar(comprar_producto))
    else:
        print(pantalon.comprar(comprar_producto))
