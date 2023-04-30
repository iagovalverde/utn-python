'''
Desafio Integrador 02
Nombre: Iago Valverde Pachiani
Div - 1D
'''

## 0.0 
def stark_normalizar_datos(lista:list, clave:str)->list:
    '''
    Brief: Convierte al tipo de dato correcto las claves de la lista (apenas las que representan datos numéricos)   
    Parameters:
        lista: list -> lista sobre la que voy a convertir las claves
        clave: str -> la clave con la cual realizo la conversion en la lista
    Return: la lista con los datos normalizados
    '''
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
    '''
    Brief: toma por un diccionario los elementos de la lista y formatea su nombre   
    Parameters:
        diccionario: dict -> que representa cada elemento de la lista
    Return: una string que contiene el nombre del elemento formateado
    '''
    nombre_elemento = f"Nombre: {diccionario['nombre']}"
    return nombre_elemento

## 1.2
def imprimir_dato(dato:str):
    '''
    Brief: recibe por parametro una string y la imprime en la consola  
    Parameters:
        dato: str -> string que será mostrada en la consola
    Return: no retorna nada
    '''
    print(dato)

## 1.3
def stark_imprimir_nombres_heroes(lista:list):
    '''
    Brief: imprime la lista con cada uno de sus elementos
    Parameters:
        lista: list -> lista con sus elementos que será mostrada en consola
    Return: -1 apenas en caso de que la lista esté vacía
    '''
    if len(lista) == 0:
        return -1
    else:
        for elemento in lista:
            nombre = obtener_nombre(elemento)
            imprimir_dato(nombre)

## 2
def obtener_nombre_y_dato(diccionario:dict, clave:str)->str:
    '''
    Brief: toma por un diccionario los elementos de la lista y una de sus claves, formateando esos datos   
    Parameters:
        diccionario: dict -> que representa cada elemento de la lista y una de sus claves
    Return: una string que contiene el nombre del elemento y una de sus claves, ambos formateados
    '''
    if clave in diccionario:
        nombre_y_dato = f"Nombre: {diccionario['nombre']} | {clave}: {diccionario[clave]}"
        return nombre_y_dato

## 3
def stark_imprimir_nombres_alturas(lista:list, clave:str):
    '''
    Brief: itera la lista e imprime el nombre y la clave de cada elemento       
    Parameters:
        lista: list -> que será iterada y de cada elemento, mostrar su nombre
        clave: str -> de cada elemento, será mostrado su nombre con esa clave
    Return: -1 apenas en caso de que la lista esté vacía
    '''
    if len(lista) == 0:
        return -1
    else:
        for elemento in lista:
            nombre_y_clave = obtener_nombre_y_dato(elemento, clave)
            print(nombre_y_clave)

## 4.1 
def calcular_max(lista:list, dato:str):
    '''
    Brief: evalua del dato elegido, cual es el dato máximo de la lista iterada
    Parameters:
        lista: list -> que será iterada buscando los datos de cada elemento
        dato: str -> compara los datos de cada elemento, buscando el mayor
    Return: el valor máximo del dato elegido (puede ser un int o un float - depende del dato analisado)
    '''
    flag_maximo = True
    stark_normalizar_datos(lista, dato)
    for elemento in lista:
        if flag_maximo == True or elemento[dato] > dato_maximo:
            dato_maximo = elemento[dato]
            flag_maximo = False
    return dato_maximo

## 4.2
def calcular_min(lista:list, dato:str):
    '''
    Brief: evalua del dato elegido, cual es el dato minimo de la lista iterada
    Parameters:
        lista: list -> que será iterada buscando los datos de cada elemento
        dato: str -> compara los datos de cada elemento, buscando el menor
    Return: el valor minimo del dato elegido (puede ser un int o un float - depende del dato analisado)
    '''
    flag_minimo = True
    stark_normalizar_datos(lista, dato)
    for elemento in lista:
        if flag_minimo == True or elemento[dato] < dato_minimo:
            dato_minimo = elemento[dato]
            flag_minimo = False
    return dato_minimo

## 4.3 
def calcular_max_min_dato(lista:list, tipo_calculo:str, dato:str):
    '''
    Brief: toma el elemento que cumple con el dato max/min de la lista y retorna ese elemento
    Parameters:
        lista: list -> que será iterada buscando el elemento que posee el dato max/min de la lista
        tipo_calculo: str -> una string que toma como valores 'maximo' o 'minimo' para comparar los datos de los elementos
        dato: str -> la key de los elementos de la lista que será comparada con las demás keys de los elementos
    Return: el elemento que posee el dato max/min de toda la lista
    '''
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

# 4.4 
def stark_calcular_imprimir_heroe(lista:list, tipo_calculo:str, dato:str):
    '''
    Brief: obtiene el elemento posee el dato max/min de la lista e imprime su nombre y dato
    Parameters:
        lista: list -> que será iterada buscando el elemento que posee el dato max/min de la lista
        tipo_calculo -> una string que toma como valores 'maximo' o 'minimo' para comparar los datos de los elementos
        dato: str -> la key de los elementos de la lista que será comparada con las demás keys de los elementos
    Return: -1 apenas en caso de que la lista esté vacía
    '''
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

# 5.1
def sumar_dato_heroe(lista:list, dato:str):
    '''
    Brief: suma entre uno de los datos de todos los elementos de la lista
    Parameters:
        lista: list -> que será iterada buscando los datos de cada elemento
        dato: str -> dato que tendrá sus valores sumados
    Return: el valor de la suma (int o float)
    '''
    suma = 0
    stark_normalizar_datos(lista, dato)
    for elemento in lista:
        if isinstance(elemento, dict) and elemento[dato] is not None:
            suma += elemento[dato]
    return suma

# 5.2
def dividir(dividendo:float, divisor:int):
    '''
    Brief: hace una division entre dividendo y divisor
    Parameters:
        dividendo: float -> valor que será dividido
        divisor: int -> valor que hará la division
    Return: 0 si el divisor es igual a cero o el resultado de la division si el divisor no es cero
    '''
    if divisor == 0:
        return 0
    else:
        resultado_division = dividendo / divisor
    return resultado_division

# 5.3
def calcular_promedio(lista:list, dato:str):
    '''
    Brief: calcula el promedio de un dato entre todos los elementos de la lista
    Parameters:
        lista: list -> de donde se toman los datos de cada elemento
        dato: str -> el cual se calculará el promedio
    Return: el valor del promedio de los datos de todos los elementos de la lista
    '''
    cantidad_elementos = len(lista)
    resultado_suma = sumar_dato_heroe(lista, dato)
    if cantidad_elementos > 0:
        promedio = dividir(resultado_suma, cantidad_elementos)
    else:
        promedio = 0
    return promedio

# 5.4
def stark_calcular_imprimir_promedio_altura(lista:list):
    '''
    Brief: imprime el promedio de las alturas de los elementos de la lista
    Parameters:
        lista: list -> de donde se toman las alturas de cada elemento
    Return: el valor del promedio de las alturas de todos los elementos de la lista, en caso de que la lista esté vacía retornará -1
    '''
    if len(lista) == 0:
        return -1
    
    suma_altura = sumar_dato_heroe(lista, 'altura')
    resultado_promedio = calcular_promedio(lista, 'altura')
    imprimir_dato(f"El promedio de altura entre los heroes: {resultado_promedio}")

# 6.1
def imprimir_menu():
    '''
    Brief: recibe el menú de opciones
    Parameters: no tiene
    Return: no retorna nada
    '''
    imprimir_dato("1. Mostrar nombre de los heroes" 
                f"\n2. Mostrar nombre y altura de los heroes"
                f"\n3. Mostrar altura maxima entre los heroes"
                f"\n4. Mostrar altura minima entre los heroes"
                f"\n5. Calcular promedio de las alturas"
                f"\n6. Mostrar nombre del heroe más alto y del más bajo"
                f"\n7. Calcular peso máximo y minimo de los heroes"
                f"\n8. Salir"
)

# 6.2
def validar_entero(numero:str)-> bool:
    '''
    Brief: recibe una string de numero y verifica si está conformada únicamente por dígitos
    Parameters: 
        numero: str -> numero el cual será verificado si está conformado apenas por dígitos
    Return: retorna un booleano: verdadero si el numero es apenas dígitos o falso sí no es apenas dígitos
    '''
    return numero.isdigit()

# 6.3
def stark_menu_principal()->int:
    '''
    Brief: imprime el menú de opciones para que el usuario elija, validando la opcion
    Parameters: no tiene
    Return: retorna la opcion como entero, o -1 en caso de que la opcion no sea apenas dígitos
    '''
    imprimir_menu()
    respuesta = input("Ingrese una opcion:")
    if validar_entero(respuesta) == True:
        respuesta = int(respuesta)
        return respuesta
    else:
        return -1

# 7
def stark_marvel_app(lista:list):
    '''
    Brief: recibe la opcion del usuario e imprime la respuesta por consola
    Parameters: 
        lista: list -> la lista por la cual se tomarán los elementos y datos
    Return: no retorna nada
    '''
    while True:
        opcion_elegida = stark_menu_principal()
        match opcion_elegida:
            case 1:
                stark_imprimir_nombres_heroes(lista)
            case 2:
                stark_imprimir_nombres_alturas(lista, 'altura')
            case 3:
                stark_calcular_imprimir_heroe(lista, 'maximo', 'altura')
            case 4:
                stark_calcular_imprimir_heroe(lista, 'minimo', 'altura')
            case 5:
                stark_calcular_imprimir_promedio_altura(lista)
            case 6:
                stark_calcular_imprimir_heroe(lista, 'maximo', 'altura')
                stark_calcular_imprimir_heroe(lista, 'minimo', 'altura')
            case 7:
                stark_calcular_imprimir_heroe(lista, 'maximo', 'peso')
                stark_calcular_imprimir_heroe(lista, 'minimo', 'peso')
            case 8:
                break
            case _:
                print("[ERROR] Opcion incorrecta.")