#1
'''
# Inicializar la lista de productos
productos = [
    {"nombre": "botellas", "cantidad": 10, "ubicacion": (1, 2)},
    {"nombre": "fideos", "cantidad": 15, "ubicacion": (2, 3)},
    {"nombre": "frascos", "cantidad": 5, "ubicacion": (1, 4)},
    {"nombre": "leche", "cantidad": 20, "ubicacion": (3, 4)},
]


def mostrar_stock():
    print("Stock de productos:")
    for producto in productos:
        print(f"Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}, Ubicación: {producto['ubicacion']}")

def agregar_producto(nombre, cantidad, ubicacion):
    for producto in productos:
        if producto['nombre'] == nombre and producto['ubicacion'] == ubicacion:
            producto['cantidad'] += cantidad
            return
    productos.append({"nombre": nombre, "cantidad": cantidad, "ubicacion": ubicacion})

'''


def mostrar_menu():
    print("1 - Alta de productos")
    print("2 - Baja de productos")
    print("3 - Modificar productos")
    print("4 - Listar productos")
    print("5 - Lista de productos ordenado por nombre")
    print("6 - Salir")


def alta_producto(productos):
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad: "))
    fila = int(input("Ingrese la fila: "))
    columna = int(input("Ingrese la columna: "))
    productos.append([nombre, cantidad, (fila, columna)])
    print(f"Producto '{nombre}' agregado.")

def baja_producto(productos):
    nombre = input("Ingrese el nombre del producto a eliminar: ")
    for producto in productos:
        if producto[0] == nombre:
            productos.remove(producto)
            print(f"Producto '{nombre}' eliminado.")
            return
    print(f"Producto '{nombre}' no encontrado.")

def modificar_producto(productos):
    nombre = input("Ingrese el nombre del producto a modificar: ")
    for producto in productos:
        if producto[0] == nombre:
            nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
            nueva_fila = int(input("Ingrese la nueva fila: "))
            nueva_columna = int(input("Ingrese la nueva columna: "))
            producto[1] = nueva_cantidad
            producto[2] = (nueva_fila, nueva_columna)
            print(f"Producto '{nombre}' modificado.")
            return
    print(f"Producto '{nombre}' no encontrado.")

def listar_productos(productos):
    for producto in productos:
        print(f"Nombre: {producto[0]}, Cantidad: {producto[1]}, Ubicación: {producto[2]}")

def listar_ordenados(productos):

    n = len(productos)
    for i in range(n):
        for j in range(n - 1):
            if productos[j][0] > productos[j + 1][0]:
                productos[j], productos[j + 1] = productos[j + 1], productos[j]

    listar_productos(productos)

#4


def main():
    productos = []
    while True:
        mostrar_menu()
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            alta_producto(productos)
        elif opcion == 2:
            if not productos:
                print("Error: No hay productos para eliminar.")
            else:
                baja_producto(productos)
        elif opcion == 3:
            if not productos:
                print("Error: No hay productos para modificar.")
            else:
                modificar_producto(productos)
        elif opcion == 4:
            listar_productos(productos)
        elif opcion == 5:
            listar_ordenados(productos)
        elif opcion == 6:
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")



#Ej 5: 
estanteria = [
    [["to12", 65], ["to16", 86], ["to20", 30], ["to25", 45]],
    [["to35", 73], ["to40", 85], ["to45", 89], ["ta4", 58]],
    [["ta5", 48], ["ta6", 64], ["ta8", 36], ["ta10", 96]],
    [["ta7", 72], ["ta12", 78], ["ta14", 71], ["ta15", 0]],
]
#6
def mostrar_menu_ferreteria():
    print("1 - Reponer mercadería")
    print("2 - Vender mercadería")
    print("3 - Listar inventario")
    print("4 - Salir")

#7

def reponer_mercaderia(estanteria):
    nombre = input("Ingrese el nombre del artículo: ")
    cantidad = int(input("Ingrese la cantidad a reponer: "))

#terminar
def vender_mercaderia(estanteria):
    nombre = input("Ingrese el nombre del artículo: ")
    cantidad = int(input("Ingrese la cantidad a vender: "))
    for fila in estanteria:
        for cajon in fila:
            if cajon[0] == nombre:
                if cajon[1] >= cantidad:
                    cajon[1] -= cantidad
                    print(f"Vendidos {cantidad} de '{nombre}', stock restante: {cajon[1]}.")
                else:
                    print(f"No hay suficiente stock de '{nombre}'.")
                return
    print(f"Artículo '{nombre}' no encontrado.")


def lista_inventario(estanteria):
    for fila in estanteria:
        for cajon in fila:
            print(f"Nombre: {cajon[0]}, Cantidad: {cajon[1]}")



#8
def main_ferreteria():
    while True:
        mostrar_menu_ferreteria()
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            reponer_mercaderia(estanteria)
        elif opcion == 2:
            vender_mercaderia(estanteria)
        elif opcion == 3:
            lista_inventario(estanteria)
        elif opcion == 4:
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")
