from GestorProductos import GestorProducto

def menu():
    op = int(input("""
                                                            MENÚ DE OPCIONES
                1) Cargar productos
                2) Agregar productos al gestor
                3) Mostrar productos actualmente cargados
                4) Ingresar posición de la lista a la que se desea acceder para mostrar qué tipo de producto se encuentra almacenado
                5) Mostrar cantidad de productos de cada tipo
                6) Mostrar nombre, país de origen, temperatura de mantenimiento recomendada e importe de venta de todos los productos
                0) SALIR
                Su opción --> """))
    return op

if __name__ == '__main__':
    opcion = menu()
    gestor = GestorProducto()

    while opcion != 0:
        if opcion == 1:
            gestor.cargarProductos()
            print("\nProductos cargados exitosamente.")
        elif opcion == 2:
            gestor.agregarProductoManual()
        elif opcion == 3:
            gestor.mostrarProductos()
        elif opcion == 4:
            pos = int(input("\nIngrese la posición: "))
            gestor.mostrarProductoPos(pos)
        elif opcion == 5:
            gestor.mostrarCantProd()
        elif opcion == 6:
            gestor.mostrarColeccion()
        opcion = menu()
