'''
#1

def ordenar_nombres(nombres, edades):
    combinados = []
    for i in range(len(nombres)):
        combinados.append((nombres[i], edades[i]))
    n = len(combinados)
    for i in range(n):
        for j in range(n - 1):
            if combinados[j][0] > combinados[j + 1][0]:
                # Intercambiar las tuplas
                combinados[j], combinados[j + 1] = combinados[j + 1], combinados[j]

    nombres_ordenados = []
    edades_ordenadas = []
    for nombre, edad in combinados:
        nombres_ordenados.append(nombre)
        edades_ordenadas.append(edad)

    return nombres_ordenados, edades_ordenadas


def ordenar_nombres_y_puntos(nombres, puntos):

    combinados = []
    for i in range(len(nombres)):
        combinados.append((nombres[i], puntos[i]))

    n = len(combinados)
    for i in range(n):
        for j in range(n - 1):
            if combinados[j][0] > combinados[j + 1][0]:
                combinados[j], combinados[j + 1] = combinados[j + 1], combinados[j]
            elif combinados[j][0] == combinados[j + 1][0]:
                if combinados[j][1] < combinados[j + 1][1]:
                    combinados[j], combinados[j + 1] = combinados[j + 1], combinados[j]

    nombres_ordenados = []
    puntos_ordenados = []
    for nombre, punto in combinados:
        nombres_ordenados.append(nombre)
        puntos_ordenados.append(punto)

    return nombres_ordenados, puntos_ordenados



#Ejercicio 3:

Estudiantes = ["Ana","Luis","Juan","Sol","Roberto","Sonia","María","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "María"] 
Apellidos = [“Sosa”,”Gutierrez”,”Alsina”,”Martinez”,”Sosa”,”Ramirez”,”Perez”,”Lopez”,”Arregui”,”Mitre”,”Andrade”,”Loza”,”Antares”,”Roca”,”Perez”] 
Nota = [8,4,9,10,8,6,4,8,7,5,6,7,10,4,8] 

def ordenar_estudiantes(apellidos, nombres, notas):
    combinados = []
    for i in range(len(apellidos)):
        combinados.append((apellidos[i], nombres[i], notas[i]))

    n = len(combinados)
    for i in range(n):
        for j in range(n - 1):
            if combinados[j][0] > combinados[j + 1][0]:
                combinados[j], combinados[j + 1] = combinados[j + 1], combinados[j]
            elif combinados[j][0] == combinados[j + 1][0]:
                if combinados[j][1] > combinados[j + 1][1]:
                    combinados[j], combinados[j + 1] = combinados[j + 1], combinados[j]
                elif combinados[j][1] == combinados[j + 1][1]:
                    if combinados[j][2] < combinados[j + 1][2]:
                        combinados[j], combinados[j + 1] = combinados[j + 1], combinados[j]

    apellidos_ordenados = []
    nombres_ordenados = []
    notas_ordenadas = []
    for apellido, nombre, nota in combinados:
        apellidos_ordenados.append(apellido)
        nombres_ordenados.append(nombre)
        notas_ordenadas.append(nota)

    return apellidos_ordenados, nombres_ordenados, notas_ordenadas




#Ejercicio 4


def menu():
    while True:
        print("1. Importar listas")
        print("2. Listar usuarios de México")
        print("3. Listar nombre, mail y teléfono de usuarios de Brasil")
        print("4. Listar usuarios más jóvenes")
        print("5. Promedio de edad de los usuarios")
        print("6. Usuario de mayor edad en Brasil")
        print("7. Listar usuarios de México y Brasil con código postal > 8000")
        print("8. Listar nombre, mail y teléfono de italianos mayores de 40")
        print("9. Listar usuarios de México ordenados por nombre")
        print("10. Listar usuarios más jóvenes ordenados por edad")
        print("11. Listar usuarios de México y Brasil con código postal > 8000 ordenado por nombre y edad")
        print("12. Salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            importar_listas() 
        elif opcion == 2:
            listar_usuarios_mexico()  
        elif opcion == 12:
            break


def usuarios_mexico(usuarios):
    for usuario in usuarios:
        if usuario["pais"] == "México":
            print(usuario)

def datos_brasil(usuarios):
    for usuario in usuarios:
        if usuario["pais"] == "Brasil":
            print(usuario["nombre"], usuario["mail"], usuario["telefono"])

def mas_jovenes(usuarios):
    if not usuarios:
        return
    menor_edad = min(usuario["edad"] for usuario in usuarios)
    for usuario in usuarios:
        if usuario["edad"] == menor_edad:
            print(usuario)

def promedio_edad(usuarios):
    if not usuarios:
        return 0
    total_edad = sum(usuario["edad"] for usuario in usuarios)
    return total_edad / len(usuarios)

def mayor_brasil(usuarios):
    mayor_edad = -1
    usuario_mayor = None
    for usuario in usuarios:
        if usuario["pais"] == "Brasil" and usuario["edad"] > mayor_edad:
            mayor_edad = usuario["edad"]
            usuario_mayor = usuario
    if usuario_mayor:
        print(usuario_mayor)

def usuarios_cp(usuarios):
    for usuario in usuarios:
        if usuario["codigo_postal"] > 8000 and (usuario["pais"] == "México" or usuario["pais"] == "Brasil"):
            print(usuario)

def italianos_mayores_40(usuarios):
    for usuario in usuarios:
        if usuario["pais"] == "Italia" and usuario["edad"] > 40:
            print(usuario["nombre"], usuario["mail"], usuario["telefono"])

def mexico_ordenado(usuarios):
    usuarios_mexico = [usuario for usuario in usuarios if usuario["pais"] == "México"]
    for i in range(len(usuarios_mexico)):
        for j in range(len(usuarios_mexico) - 1):
            if usuarios_mexico[j]["nombre"] > usuarios_mexico[j + 1]["nombre"]:
                usuarios_mexico[j], usuarios_mexico[j + 1] = usuarios_mexico[j + 1], usuarios_mexico[j]
    for usuario in usuarios_mexico:
        print(usuario)

def jovenes_ordenados(usuarios):
    if not usuarios:
        return
    menor_edad = min(usuario["edad"] for usuario in usuarios)
    jovenes = [usuario for usuario in usuarios if usuario["edad"] == menor_edad]
    jovenes.sort(key=lambda x: (x["edad"], x["nombre"]))  # Cambia esto a una ordenación manual si es necesario
    for usuario in jovenes:
        print(usuario)

def cp_ordenado(usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["codigo_postal"] > 8000 and (usuario["pais"] == "México" or usuario["pais"] == "Brasil")]
    for i in range(len(usuarios_filtrados)):
        for j in range(len(usuarios_filtrados) - 1):
            if (usuarios_filtrados[j]["nombre"] > usuarios_filtrados[j + 1]["nombre"] or
                (usuarios_filtrados[j]["nombre"] == usuarios_filtrados[j + 1]["nombre"] and usuarios_filtrados[j]["edad"] < usuarios_filtrados[j + 1]["edad"])):
                usuarios_filtrados[j], usuarios_filtrados[j + 1] = usuarios_filtrados[j + 1], usuarios_filtrados[j]
    for usuario in usuarios_filtrados:
        print(usuario)

'''