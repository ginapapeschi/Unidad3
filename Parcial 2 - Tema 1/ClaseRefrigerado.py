from ClaseProducto import Producto

class Refrigerado(Producto):
    __codigo: str

    def __init__(self, nom, fechaE, fechaV, temp, pais, num, costo, cod):
        super().__init__(nom, fechaE, fechaV, temp, pais, num, costo)
        self.__codigo = cod
    
    def __str__(self):
        return f"\nNombre del producto: {self._Producto__nombre}\nFecha de envasado: {self._Producto__fechaEnv}\nFecha de vencimiento: {self._Producto__fechaVenc}\nTemperatura: {self._Producto__temperatura}\nPaís de origen: {self._Producto__paisOrigen}\nNúmero de lote: {self._Producto__numLote}\nCosto base: ${self._Producto__costo}\nCódigo: {self.__codigo}"    

    def getCodigo(self):
        return self.__codigo
    
    def importeVenta(self):
        pass

