#1
'''
def suma_naturales(numero: int) -> int:
    if numero == 0:  # Caso base: si el número es 0, la suma es 0
        return 0
    return numero + sumar_naturales(numero - 1)  # Caso recursivo: sumar el número actual y la suma de los números anteriores

'''
#2
'''
def calcular_potencia(base: int, exponente: int) -> int:
    if exponente == 0:
        return 1
    elif exponente > 0:
        return base * calcular_potencia (base, exponente - 1)
    else:
        return 1 / calcular_potencia (base, -exponente)

'''

#3
'''
def sumar_digitos (numero: int) -> int:
    if numero == 0:
        return 0
    return (numero % 10) + sumar_digitos (numero // 10)
'''

#4
'''
def get_int (mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int:
    numero_reintentos =
    for _ in range (reintentos):
        while:
            valor = int (input(mensaje))
            if minimo <= valor <= maximo:
                return valor
            numero_reintentos += 1
            elif:
                if numero_reintentos == reintentos:
                    print(mensaje_error)
                    print("Se alcanzó el número máximo de reintentos.")
        break

def calcular_fibonacci(numero: int) -> int:
    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    return calcular_fibonacci(numero - 1) + calcular_fibonacci(numero - 2)

numero = get_int("Ingresa un número entero positivo: ", "Error. Intenta de nuevo.", 0, 30, 3)

resultado = calcular_fibonacci(numero)

print(f"El número de Fibonacci para {numero} es: {resultado}")

'''