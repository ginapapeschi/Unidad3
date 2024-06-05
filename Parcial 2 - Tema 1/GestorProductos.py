from ClaseRefrigerado import Refrigerado
from ClaseCongelado import Congelado
import csv

class GestorProducto:
    __lista: list

    def __init__(self):
        self.__lista = []

    def agregarProducto(self, nuevo):
        self.__lista.append(nuevo)

    def cargarProductos(self):
        archivo = open("productos.csv")
        reader = csv.reader (archivo, delimiter = ";")
        next(reader)
        for fila in reader:
            if fila[0] == "C":
                congelado = (Congelado(fila[1], fila[2], fila[3], float(fila[4]), fila[5], (fila[6]), float(fila[7]), int(fila[8]), int(fila[9]), int(fila[10]), int(fila[11]), fila[12]))
                self.agregarProducto(congelado)             # gina pelotuda es directamente self.método no self.__lista.MadreEnConcha()
            elif fila[0] == "R":
                refrigerado = (Refrigerado(fila[1], fila[2], fila[3], float(fila[4]), fila[5], (fila[6]), float(fila[7]), (fila[8])))
                self.agregarProducto(refrigerado)           # gina pelotuda es directamente self.método no self.__lista.MadreEnConcha()
        archivo.close()

    def mostrarProductos(self):
        print("\nLISTA DE PRODUCTOS:")
        for producto in self.__lista:
            print(producto)

    def agregarProductoManual(self):
        opcion = int(input("\nIngrese el tipo de producto que quiere cargar: [1] Congelado, [2] Refrigerado, [0] Finalizar: "))
        while opcion != 0:
            if opcion == 1:
                nombre = input("Ingrese nombre del congelado: ")
                fechaEnv = input("Ingrese fecha de envasado: ")
                fechaVenc = input("Ingrese fecha de vencimiento: ")
                temperatura = input("Ingrese temperatura de mantenimiento recomendada: ")
                paisOrigen = input("Ingrese país de origen del congelado: ")
                numLote = input("Ingrese número de lote: ")
                costo = input("Ingrese costo base: $")
                nitro = input("Ingrese porcentaje de nitrógeno: %")
                oxi = input("Ingrese porcentaje de oxígeno: %")
                dioxi = input("Ingrese porcentaje de dióxido de carbono: %")
                vapor = input("Ingrese porcentaje de vapor: %")
                metodoCong = input("Ingrese método de congelación: ")
                congelado = (Congelado(nombre, fechaEnv, fechaVenc, temperatura, paisOrigen, numLote, costo, nitro, oxi, dioxi, vapor, metodoCong))
                self.agregarProducto(congelado)
                print("Producto congelado cargado exitosamente.")
            
            elif opcion == 2:
                nombre = input("Ingrese nombre del refrigerado: ")
                fechaEnv = input("Ingrese fecha de envasado: ")
                fechaVenc = input("Ingrese fecha de vencimiento: ")
                temperatura = input("Ingrese temperatura de mantenimiento recomendada: ")
                paisOrigen = input("Ingrese país de origen del refrigerado: ")
                numLote = input("Ingrese número de lote: ")
                costo = input("Ingrese costo base: $")
                codigo = input("Ingrese código del organismo de supervisión alimentaria: ")
                refrigerado = (Refrigerado(nombre, fechaEnv, fechaVenc, temperatura, paisOrigen, numLote, costo, codigo))
                self.agregarProducto(refrigerado)
                print("Producto refrigerado cargado exitosamente.")
                
            opcion = int(input("\nIngrese el tipo de producto que quiere cargar: [1] Congelado, [2] Refrigerado, [0] Finalizar: "))
    
    def mostrarProductoPos(self, pos):
        if isinstance (self.__lista[pos], Congelado):
            print(f"\nEl tipo de producto en la posición {pos} es congelado.")
        elif isinstance (self.__lista[pos], Refrigerado):
            print(f"\nEl tipo de producto en la posición {pos} es refrigerado.")

    def mostrarCantProd(self):
        contC = 0
        contR = 0
        for producto in self.__lista:
            if isinstance (producto, Congelado):
                contC += 1
            elif isinstance (producto, Refrigerado):
                contR += 1
        print(f"\nLa cantidad de productos congelados: {contC}.")
        print(f"La cantidad de productos refrigerados: {contR}.")

    def mostrarColeccion(self):
        print("\nColección de productos:")
        for producto in self.__lista:
            if isinstance(producto, Congelado):
                importeC = producto.importeVenta()
                print(f"""
Tipo de producto: Congelado
Nombre: {producto.getNombre()}
País de origen: {producto.getPais()}
Temperatura de mantenimiento recomendada: {producto.getTemperatura()}
Importe de venta: ${importeC:.2f}""")
            elif isinstance(producto, Refrigerado):
                importeR = producto.importeVenta()
                print(f"""
Tipo de producto: Refrigerado
Nombre: {producto.getNombre()}
País de origen: {producto.getPais()}
Temperatura de mantenimiento recomendada: {producto.getTemperatura()}
Importe de venta: ${importeR:.2f}""")