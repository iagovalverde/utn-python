'''
Desafio Integrador 02
Nombre: Iago Valverde Pachiani
Div - 1D
'''

from data_stark import lista_personajes

## 0.0 
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

## 1.1
def obtener_nombre(diccionario:dict)->str:
    nombre_elemento = f"Nombre: {diccionario['nombre']}"
    return nombre_elemento

## 1.2
def imprimir_dato(dato:str):
    print(dato)

## 1.3
def stark_imprimir_nombres_heroes(lista:list):
    if len(lista) == 0:
        return -1
    else:
        for elemento in lista:
            nombre = obtener_nombre(elemento)
            imprimir_dato(nombre)

## 2
def obtener_nombre_y_dato(diccionario_nombre:dict, clave):
    if clave in diccionario_nombre:
        nombre_y_dato = f"Nombre: {diccionario_nombre['nombre']} | {clave}: {diccionario_nombre[clave]}"
        return nombre_y_dato

## 3
def stark_imprimir_nombres_alturas(lista:list, clave):
    if len(lista) == 0:
        return -1
    else:
        for elemento in lista:
            nombre_y_clave = obtener_nombre_y_dato(elemento, clave)
            print(nombre_y_clave)

## 4.1 
def calcular_max(lista:list, dato:str):
    flag_maximo = True
    for elemento in lista:
        if flag_maximo == True or elemento[dato] > dato:
            elemento[dato] = dato
            flag_maximo = False
    return elemento[dato]

## 4.2
def calcular_min(lista:list, dato:str):
    flag_minimo = True
    for elemento in lista:
        if flag_minimo == True or elemento[dato] < dato:
            elemento[dato] = dato
            flag_minimo = False
        return elemento[dato]

## 4.3 esta MAL
def calcular_max_min_dato(lista:list, tipo_calculo:str, dato:str):
    if tipo_calculo == 'maximo':
        nombre_elemento = calcular_max(lista, dato)
    else:
        if tipo_calculo == 'minimo':
            nombre_elemento = calcular_min(lista, dato)
    print(nombre_elemento)        
    return nombre_elemento

calcular_max_min_dato(lista_personajes, 'maximo', 'altura')