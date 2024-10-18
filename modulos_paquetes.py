'''


def get_int(mensaje: str, mensaje_error: str, mínimo: int, máximo: int, reintentos: int) -> int | None:
    for _ in range(reintentos):
        valor = input(mensaje)
        
        es_valido = True
        
        if len(valor) > 0:  
            if valor[0] == '-':
                if len(valor) == 1:  # Solo el signo negativo
                    es_valido = False
                else:
                    for c in valor[1:]:
                        if c not in '0123456789':
                            es_valido = False
                            break
            else:
                for c in valor:
                    if c not in '0123456789':
                        es_valido = False
                        break
        else:
            es_valido = False  #no valido sin caract

        if es_valido:
            valor = int(valor)
            if mínimo <= valor <= máximo:
                return valor
            else:
                print(mensaje_error)
        else:
            print(mensaje_error)
    
    return None




#2

def get_string(longitud: int) -> str | None:
    pass


def get_string(longitud: int) -> str | None:
    valor = input("Ingrese una cadena: ")
    if len(valor) <= longitud:
        return valor
    else:
        print(f"Error: La cadena debe tener como máximo {longitud} caracteres.")
        return None



#3  estan en sus carpetas




#4me faltan los usuarios de los profes que no me di cuenta de copiarlos 
'''