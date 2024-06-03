from GestorProductos import GestorProducto

def menu():
    op = int(input("""
                            MENÚ DE OPCIONES
                1) Cargar productos
                2) Agregar productos al gestor
                3) Mostrar productos actualmente cargados
                4)
                5)
                6)
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
            pass
        elif opcion == 5:
            pass
        elif opcion == 6:
            pass
        opcion = menu()
