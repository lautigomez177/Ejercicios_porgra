#1
'''
def mostrar_numero(numero):
    print(numero)


resultado = mostrar_numero(18)
'''

#2
'''
def solicitar_numero():
    numero = input("Ingrese un número: ")
    numero = int(numero)
    return numero

numero_ingresado = solicitar_numero()

print(f"El número ingresado es: {numero_ingresado}")
'''

#3
'''
def es_par(numero):
    return numero % 2 == 0

numero_ingresado = float(input("Ingrese un número: "))
resultado = es_par(numero_ingresado)

print(f"El número {numero_ingresado} es par: {resultado}")
'''



#4 
'''
def mostrar_rango_vof(desde, hasta):
    
    numero = float(input("Ingrese un número: "))
    if desde <= numero <= hasta:
        print(f"El número ingresado es: {numero}")
        return True
    else:
        print(f"El número ingresado {numero} no está dentro del rango [{desde}, {hasta}].")
        return False

def prueba():

    desde = float(input("Ingrese el límite inferior del rango: "))
    hasta = float(input("Ingrese el límite superior del rango: "))
    
    resultado = mostrar_rango_vof(desde, hasta)
    
    if resultado:
        print("El número está dentro del rango y ha sido mostrado.")
    else:
        print("El número no está dentro del rango.")


ejecutar = prueba()
'''


#5
'''
# Restar1: Recibe dos enteros y retorna el resultado de la resta
def Restar1(a: int, b: int) -> int:
    return a - b

# Restar2: No recibe argumentos y retorna un entero fijo
def Restar2() -> int:
    return 10  # Ejemplo de retorno fijo

# Restar3: Recibe dos enteros y solo imprime el resultado de la resta
def Restar3(a: int, b: int):
    resultado = a - b
    print(f"El resultado de Restar3({a}, {b}) es: {resultado}")

# Restar4: No recibe argumentos y solo imprime un mensaje
def Restar4():
    print("Esta función no realiza ninguna operación de resta.")

# Programa principal para probar las funciones
def main():
    # Probar Restar1
    resultado1 = Restar1(15, 5)
    print(f"Resultado de Restar1: {resultado1}")

    # Probar Restar2
    resultado2 = Restar2()
    print(f"Resultado de Restar2: {resultado2}")

    # Probar Restar3
    Restar3(20, 7)

    # Probar Restar4
    Restar4()

# Llamar al programa principal
if __name__ == "__main__":
    main()
'''


#6

'''
def realizarDescuento(valor: float) -> float:
    """
    Aplica un descuento del 5% al valor proporcionado.

    :param valor: El valor al cual se le aplicará el descuento.
    :return: El valor después de aplicar el descuento.
    """
    descuento = 0.05  # 5% de descuento
    valor_descuento = valor * (1 - descuento)
    return valor_descuento

def solicitar_numero():
    """
    Solicita al usuario que ingrese un número y lo valida entre 10 y 100.
    
    :return: Un número válido entre 10 y 100.
    """
    numero_valido = False
    while not numero_valido:
        # Solicitar al usuario que ingrese un número
        entrada = input("Ingrese un número entre 10 y 100: ")
        
        # Verificar si la entrada es un número y está dentro del rango
        if entrada.replace('.', '', 1).isdigit():  # Verifica si es un número (permitiendo un punto decimal)
            numero = float(entrada)
            if 10 <= numero <= 100:
                numero_valido = True
            else:
                print("El número ingresado no está en el rango permitido. Intente de nuevo.")
        else:
            print("Entrada inválida. Por favor ingrese un número válido.")

    return numero

def main():
    # Solicitar al usuario el número y validarlo
    numero1 = solicitar_numero()
    
    # Aplicar el descuento al número
    numero_con_descuento = realizarDescuento(numero1)
    
    # Mostrar el resultado
    print(f"El valor original es: {numero1}")
    print(f"El valor después de aplicar el descuento del 5% es: {numero_con_descuento:.2f}")

# Llamar al programa principal
if __name__ == "__main__":
    main()
'''
#7
'''
def realizarOperacion(num1: float, num2: float, operacion: str) -> float:
    """
    Realiza una operación matemática entre dos números según la operación especificada.

    :param num1: El primer número.
    :param num2: El segundo número.
    :param operacion: La operación a realizar ('s' para sumar, 'r' para restar).
    :return: El resultado de la operación.
    """
    if operacion == 's':
        return num1 + num2
    elif operacion == 'r':
        return num1 - num2
    else:
        return 0  # En un escenario real, podrías querer manejar esto de otra forma

def es_numero_valido(entrada: str) -> bool:
    """
    Verifica si la entrada es un número válido.

    :param entrada: La entrada a verificar.
    :return: True si la entrada es un número válido, False en caso contrario.
    """
    punto_encountered = False
    for char in entrada:
        if char == '.':
            if punto_encountered:  # Más de un punto decimal no es válido
                return False
            punto_encountered = True
        elif char < '0' or char > '9':  # Solo caracteres numéricos y un punto decimal son válidos
            return False
    return True

def solicitar_numero(mensaje: str) -> float:
    """
    Solicita al usuario un número y lo valida entre 10 y 100.

    :param mensaje: Mensaje que se mostrará al usuario.
    :return: Un número válido entre 10 y 100.
    """
    while True:
        entrada = input(mensaje)
        if es_numero_valido(entrada):
            numero = float(entrada)
            if 10 <= numero <= 100:
                return numero
            else:
                print("El número ingresado no está en el rango permitido. Intente de nuevo.")
        else:
            print("Entrada inválida. Por favor ingrese un número válido.")

def solicitar_operacion() -> str:
    """
    Solicita al usuario que ingrese una operación y valida la entrada.

    :return: La operación válida ('s' para sumar, 'r' para restar).
    """
    while True:
        operacion = input("Ingrese la operación ('s' para sumar, 'r' para restar): ")
        if operacion == 's' or operacion == 'r':
            return operacion
        print("Operación inválida. Por favor ingrese 's' para sumar o 'r' para restar.")

def main():
    # Solicitar los dos números y validarlos
    numero1 = solicitar_numero("Ingrese el primer número entre 10 y 100: ")
    numero2 = solicitar_numero("Ingrese el segundo número entre 10 y 100: ")
    
    # Solicitar y validar la operación
    operacion = solicitar_operacion()
    
    # Realizar la operación
    resultado = realizarOperacion(numero1, numero2, operacion)
    
    # Mostrar el resultado
    if operacion == 's':
        print(f"La suma de {numero1} y {numero2} es: {resultado}")
    elif operacion == 'r':
        print(f"La resta de {numero1} y {numero2} es: {resultado}")

'''