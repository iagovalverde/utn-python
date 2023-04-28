'''
Desafio Integrador 02
Nombre: Iago Valverde Pachiani
Div - 1D
'''

from data_stark import lista_personajes
from os import system

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
def obtener_nombre_y_dato(diccionario:dict, clave):
    if clave in diccionario:
        nombre_y_dato = f"Nombre: {diccionario['nombre']} | {clave}: {diccionario[clave]}"
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
    stark_normalizar_datos(lista, dato)
    for elemento in lista:
        if flag_maximo == True or elemento[dato] > dato_maximo:
            dato_maximo = elemento[dato]
            flag_maximo = False
    return dato_maximo

## 4.2
def calcular_min(lista:list, dato:str):
    flag_minimo = True
    stark_normalizar_datos(lista, dato)
    for elemento in lista:
        if flag_minimo == True or elemento[dato] < dato_minimo:
            dato_minimo = elemento[dato]
            flag_minimo = False
    return dato_minimo

## 4.3 
def calcular_max_min_dato(lista:list, tipo_calculo:str, dato:str):
    for elemento in lista:
        if tipo_calculo == 'maximo':
            valor_calculado = calcular_max(lista, dato) 
            if elemento[dato] == valor_calculado:
                return elemento
        else:
            if tipo_calculo == 'minimo':
                valor_calculado = calcular_min(lista, dato)
                if elemento[dato] == valor_calculado:
                    return elemento

calcular_max_min_dato(lista_personajes, 'maximo', 'peso')

# 4.4 INCOMPLETO
def stark_calcular_imprimir_heroe(lista:list, tipo_calculo:str, dato:str):
    if len(lista) == 0:
        return -1
    elemento_retornado = calcular_max_min_dato(lista, tipo_calculo, dato)
    for elemento in lista:
        if elemento == elemento_retornado:
            if tipo_calculo == 'maximo':
                nombre_y_dato = obtener_nombre_y_dato(elemento_retornado, dato)
                imprimir_dato(f"Mayor {dato}: {nombre_y_dato}")
            else:
                if tipo_calculo == 'minimo':
                    nombre_y_dato = obtener_nombre_y_dato(elemento_retornado, dato)
                    imprimir_dato(f"Menor {dato}: {nombre_y_dato}")


stark_calcular_imprimir_heroe(lista_personajes, 'menor', 'altura')

# 5.1
def sumar_dato_heroe(lista:list, dato:str):
    suma = 0
    stark_normalizar_datos(lista, dato)
    for elemento in lista:
        if isinstance(elemento, dict) and elemento[dato] is not None:
            suma += elemento[dato]
    return suma

# 5.2
def dividir(dividendo:float, divisor:int):
    if divisor == 0:
        return 0
    else:
        resultado_division = dividendo / divisor
    return resultado_division

# 5.3
def calcular_promedio(lista:list, dato:str):
    cantidad_elementos = len(lista_personajes)
    resultado_suma = sumar_dato_heroe(lista, dato)
    if cantidad_elementos > 0:
        promedio = dividir(resultado_suma, cantidad_elementos)
    else:
        promedio = 0
    return promedio

# 5.4
def stark_calcular_imprimir_promedio_altura(lista:list):
    if len(lista) == 0:
        return -1
    
    suma_altura = sumar_dato_heroe(lista, 'altura')
    resultado_promedio = calcular_promedio(lista, 'altura')
    imprimir_dato(resultado_promedio)

# stark_calcular_imprimir_promedio_altura(lista_personajes)

# 6.1
def imprimir_menu():
    imprimir_dato("1. Mostrar nombre de los heroes" 
                f"\n2. Mostrar nombre y altura de los heroes"
                f"\n3. Mostrar altura maxima entre los heroes"
                f"\n4. Mostrar altura minima entre los heroes"
                f"\n6. Mostrar nombre del heroe más alto y del más bajo"
                f"\n7. Calcular peso máximo y minimo de los heroes"
                f"\n8. Salir"
)

# 6.2
def validar_entero(numero:str):
    return numero.isdigit()

# 6.3
def stark_menu_principal():
    while True:
        imprimir_menu()
        respuesta = input("Ingrese una opcion:")
        if validar_entero(respuesta) == True:
            respuesta = int(respuesta)
            return respuesta
        else:
            return -1
        break

# 7
def stark_marvel_app(lista:list):
    opcion_elegida = stark_menu_principal()
    match opcion_elegida:
        case 1:
            stark_imprimir_nombres_heroes(lista_personajes)
        case 2:
            stark_imprimir_nombres_alturas(lista_personajes, 'altura')
        case 3:
            stark_calcular_imprimir_heroe(lista_personajes, )
        case 4:
            pass
        case 5:
            stark_calcular_imprimir_promedio_altura(lista_personajes)
        case 6:
            pass


stark_marvel_app(lista_personajes)