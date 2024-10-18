'''
#Ejercicio1

def contar_letra(letra, cadena):
        if len(letra) != 1:
            return "Error: Debe ingresar una sola letra."
        elif not cadena:
            return "Error: La cadena está vacía."
    return cadena.count(letra)



#Ejercicio 2: 
def subcadena(cadena, inicio, fin):
    if inicio < 0 or fin > len(cadena) or inicio >= fin:
        return "Error: Índices no válidos."
Usaremos la notación de slicing para obtener la subcadena.

    return cadena[inicio:fin]

(veriifcar el us del slicing)


#Ejercicio 3: 

def posic_cadena(cadena, posicion):
    if posicion < 0 or posicion >= len(cadena):
        return "Error: Posición no válida."
    return cadena[posicion]



#PARTE2

def contar_vocales(cadena):
    vocales = 'aeiou'
    conteo = {vocal: 0 for vocal in vocales}
    
    for caracter in cadena.lower():
        if caracter in conteo:
            conteo[caracter] += 1
    
    matriz = [[vocal, conteo[vocal]] for vocal in vocales]

    return matriz


def encontrar_indice(cadena, caracter):
    for i in range(len(cadena)):
        if cadena[i] == caracter:
            return i
    return -1 


def es_palindromo(cadena):
    cadena_normalizada = ""
    for c in cadena:
        if c != " ":
            cadena_normalizada += c.lower()
            
    return cadena_normalizada == cadena_normalizada[::-1] #reverso


#4

def sup_repetidos(cadena):
'''