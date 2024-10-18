#1
'''
def obtener_nombres() -> list:
    nombres = []
    for i in range(10):
        nombre = input(f"Ingrese el nombre {i + 1}: ")
        nombres.append(nombre)
    return nombres


nombres_lista = obtener_nombres()
print("Los nombres ingresados son:")
print(nombres_lista)


#2

def modificar_lista() -> list:
    lista = [0] * 10

    while True:
        posicion = input("Ingrese la posición (0-9) donde desea guardar el número: ")
        if len(posicion) == 1 and '0' <= posicion <= '9':
            posicion = int(posicion)
            break
        print("Entrada inválida. Ingrese una posición válida (0-9).")

    while True:
        numero = input("Ingrese el número a guardar: ")
        es_valido = True
        
        if numero[0] == '-' and len(numero) > 1:
            for c in numero[1:]:
                if c not in '0123456789':
                    es_valido = False
                    break
        else:
            for c in numero:
                if c not in '0123456789':
                    es_valido = False
                    break

        if es_valido:
            numero = int(numero)
            break
        print("Entrada inválida. Ingrese un número entero.")
    lista[posicion] = numero
    
    return lista

lista_modificada = modificar_lista()
print("La lista modificada es:")
print(lista_modificada)

'''
#3
'''
def obtener_numeros(minimo: int, maximo: int) -> list:
    numeros = []
    
    while len(numeros) < 10:
        numero = input(f"Ingrese un número entre {minimo} y {maximo}: ")
        es_valido = True

        if numero[0] == '-' and len(numero) > 1:
            for c in numero[1:]:
                if c not in '0123456789':
                    es_valido = False
                    break
        else:
            for c in numero:
                if c not in '0123456789':
                    es_valido = False
                    break
        
        if es_valido:
            numero = int(numero)
            if minimo <= numero <= maximo:
                numeros.append(numero)
            else:
                print(f"Error: El número debe estar entre {minimo} y {maximo}.")
        else:
            print("Entrada inválida. Debe ingresar un número entero.")
    
    return numeros

rango_minimo = int(input("Ingrese el valor mínimo del rango: "))
rango_maximo = int(input("Ingrese el valor máximo del rango: "))

if rango_minimo >= rango_maximo:
    print("El valor mínimo debe ser menor que el valor máximo.")
else:
    lista_numeros = obtener_numeros_en_rango(rango_minimo, rango_maximo)
    print("Los números ingresados son:")
    print(lista_numeros)

'''
#4
'''
def buscar_numero_en_lista(lista: list, numero: int) -> bool:
    
    return numero in lista


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numero_buscar = int(input("Ingrese el número que desea buscar en la lista: "))


existe = buscar_numero_en_lista(numeros, numero_buscar)

if existe:
    print(f"El número {numero_buscar} existe en la lista.")
else:
    print(f"El número {numero_buscar} no existe en la lista.")

'''
#5
'''
def buscar_menores(edades: list, nombres: list) -> list:
    
    menor_edad = min(edades)
    menores = []
    for i in range(len(edades)):
        if edades[i] == menor_edad:
            menores.append((nombres[i], edades[i])) 
    
    return menores

menores = buscar_menores(edades, nombres)

print("Las personas de menor edad son:")
for nombre, edad in menores:
    print(f"{nombre}: {edad} años")

'''
#6
'''
from listas_personas import nombres

def mostrar_nombres(nombres: list):
    print("Los nombres son:")
    for nombre in nombres:
        print(nombre)

mostrar_nombres(nombres)

#7
'''
