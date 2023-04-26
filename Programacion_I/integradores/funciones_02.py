'''
Desafio Integrador 02
Nombre: Iago Valverde Pachiani
Div - 1D
'''

from data_stark import lista_personajes

## 1 ##
def stark_normalizar_datos(lista:list, clave:str):
    datos_normalizados = False
    if len(lista) == 0:
        print("Error: Lista de héroes vacía")
    else:
        for elemento in lista:
            if isinstance(elemento[clave], str):
                if "." in elemento[clave] or "," in elemento[clave]:
                    elemento[clave] = float(elemento[clave])
                else:
                    elemento[clave] = int(elemento[clave])    
                datos_normalizados = True

    if datos_normalizados == True:
        print("Datos normalizados")

    return lista

def obtener_nombre(diccionario:dict)->str:
    nombre_elemento = f"Nombre: {diccionario['nombre']}"
    return nombre_elemento

def imprimir_dato(dato:str):
    print(dato)

def stark_imprimir_nombres_heroes(lista:list):
    if len(lista) == 0:
        return -1
    else:
        for elemento in lista:
            nombre = obtener_nombre(elemento)
            imprimir_dato(nombre)

## 2 ##
def obtener_nombre_y_dato(diccionario_nombre:dict, clave):
    if clave in diccionario_nombre:
        nombre_y_dato = f"Nombre: {diccionario_nombre['nombre']} | {clave}: {diccionario_nombre[clave]}"
        return nombre_y_dato

def stark_imprimir_nombres_alturas(lista:list, clave):
    if len(lista) == 0:
        return -1
    else:
        for elemento in lista:
            nombre_y_clave = obtener_nombre_y_dato(elemento, clave)
            print(nombre_y_clave)

stark_imprimir_nombres_alturas(lista_personajes, 'color_ojos')

## 3 ##


