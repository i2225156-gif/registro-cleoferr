from conexion import ConexionDB
class DProducto:
    def __init__(self):
        self.__db = ConexionDB().conexionSupabase()
        self.__nombreTabla = 'productos'
        self.__tablaCategoria = 'categoria'
    
    def __ejecutarConsultas(self, consulta, tipoConsulta = None):
        try:
            if tipoConsulta == 'SELECT':
                resultado = consulta.execute().data
                return resultado
            else:
               resultado = consulta.execute()
               return resultado 
        except Exception as e:
            raise e
    
    def mostrarProducto(self):
        consulta = self.__db.table(self.__nombreTabla).select('*')
        return self.__ejecutarConsultas(consulta, 'SELECT')
    
    def obtenerCategorias(self):
        consulta = self.__db.table(self.__tablaCategoria).select('nombre')
        return consulta.execute().data
    
    def nuevoProducto(self,producto : dict):
        consulta = self.__db.table(self.__nombreTabla).insert(producto)
        return self.__ejecutarConsultas(consulta)
    
    def actualizarProducto(self, producto):
        consulta = self.__db.table(self.__nombreTabla).update(producto).eq('id_producto', producto['id_producto'])
        return self.__ejecutarConsultas(consulta)
    
    def eliminarProducto(self, id_producto):
        consulta = self.__db.table(self.__nombreTabla).delete().eq('id_producto', id_producto)
        return self.__ejecutarConsultas(consulta)