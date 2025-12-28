from capaDatos.dProducto import DProducto

class LProducto:
    def __init__(self):
        self.__dProducto = DProducto()
    
    def mostrarProducto(self):
        return self.__dProducto.mostrarProducto()
    
    def obtenerCategorias(self):
        return self.__dProducto.obtenerCategorias()
    
    def nuevoProducto(self, producto: dict):
        self.__dProducto.nuevoProducto(producto)
        return self.__dProducto.nuevoProducto
    
    def actualizarProducto(self, producto: dict):
        return self.__dProducto.actualizarProducto(producto)
    
    def eliminarProducto(self, id_producto):
        return self.__dProducto.eliminarProducto(id_producto)