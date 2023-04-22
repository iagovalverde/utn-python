'''
Desafio Integrador 01
Nombre: Iago Valverde Pachiani
Div - 1D
'''

def mostrar_nombre_heroes(lista:list, genero:str):
    # A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
    # B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
    for heroe in lista:
        if heroe['genero'] == genero:
            print(heroe['nombre'])
        else:
            if genero == None:
                print(heroe['nombre'])

def mostrar_nombre_altura_heroes(lista:list):
    # 00C - Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
    for heroe in lista:
        print(f"{heroe['nombre']} - {heroe['altura']}")

def calcular_maxima_altura_heroes(lista:list, genero:str)->float:
    # C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
    # D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
    flag_maxima_altura = True
    for heroe in lista:
        heroe['altura'] = float(heroe['altura'])
        if heroe['genero'] == genero:
            if flag_maxima_altura == True or heroe['altura'] > maxima_altura:
                maxima_altura = heroe['altura']
                flag_maxima_altura = False
    return maxima_altura

def mostrar_heroe_mas_alto(lista:list, genero:str):
    # I. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
    altura_mas_alta = calcular_maxima_altura_heroes(lista, genero)
    for heroe in lista:
        if heroe['genero'] == genero:
            if heroe['altura'] == altura_mas_alta:
                print(f"Heroe de genero {genero} más alto: {heroe['nombre']} - Altura: {altura_mas_alta}")

def calcular_minima_altura_heroes(lista:list, genero:str)->float:
    # E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
    # F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
    flag_minima_altura = True
    for heroe in lista:
        heroe['altura'] = float(heroe['altura'])
        if heroe['genero'] == genero:
            if flag_minima_altura == True or heroe['altura'] < minima_altura:
                minima_altura = heroe['altura']
                flag_minima_altura = False
    return minima_altura

def mostrar_heroe_mas_bajo(lista:list, genero:str):
    # I. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
    for heroe in lista:
        altura_mas_baja = calcular_minima_altura_heroes(lista, genero)
        if heroe['genero'] == genero:
            if heroe['altura'] == altura_mas_baja:
                print(f"Heroe de genero {genero} más bajo: {heroe['nombre']} - Altura: {altura_mas_baja}")

def calcular_promedio_altura(lista:list, genero:str):
    # G. Recorrer la lista y determinar la altura promedio de los superhéroes de género M
    # H. Recorrer la lista y determinar la altura promedio de los superhéroes de género F
    acumulador_altura = 0
    contador_heroes = 0
    for heroe in lista:
        heroe['altura'] = float(heroe['altura'])
        if heroe['genero'] == genero:
            acumulador_altura += heroe['altura']
            contador_heroes += 1
        else:
            if genero == None:
                acumulador_altura += heroe['altura']
                contador_heroes = len(lista)
    promedio_altura = acumulador_altura / contador_heroes
    print(f"Promedio de altura de los heroes: {promedio_altura}")

def calcular_peso_max(lista:list):
    flag_peso_maximo = True
    for heroe in lista:
        heroe['peso'] = float(heroe['peso'])
        if flag_peso_maximo == True or heroe['peso'] > peso_maximo:
            peso_maximo = heroe['peso']
            flag_peso_maximo = False
    print(f"Peso máximo: {peso_maximo}")
    for heroe in lista:
        if heroe['peso'] == peso_maximo:
            print(f"Heroe más pesado: {heroe['nombre']}")

def calcular_peso_min(lista:list):
    flag_peso_minimo = True
    for heroe in lista:
        heroe['peso'] = float(heroe['peso'])
        if flag_peso_minimo == True or heroe['peso'] < peso_minimo:
            peso_minimo = heroe['peso']
            flag_peso_minimo = False
    print(f"Peso minimo: {peso_minimo}")
    for heroe in lista:
        if heroe['peso'] == peso_minimo:
            print(f"Heroe menos pesado: {heroe['nombre']}")

def calcular_tipo_caracteristica(lista:list, tipo: str):
    #J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
    #K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
    #L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No     Tiene’).
    diccionario_caracteristica = {}
    for heroe in lista:
        tipo_caracteristica = heroe[tipo]
        if tipo_caracteristica in diccionario_caracteristica:
            diccionario_caracteristica[tipo_caracteristica] += 1
        else:
            if tipo_caracteristica == "" or tipo_caracteristica is None:
                tipo_caracteristica = "No tiene"
            diccionario_caracteristica[tipo_caracteristica] = 1

    for tipo_caracteristica, cantidad_tipo in diccionario_caracteristica.items():
        print(f"Hay {cantidad_tipo} heroes con {tipo} - {tipo_caracteristica}")

def listar_heroes_caracteristica(lista:list, tipo: str):
    # M. Listar todos los superhéroes agrupados por color de ojos.
    # N. Listar todos los superhéroes agrupados por color de pelo.
    # O. Listar todos los superhéroes agrupados por tipo de inteligencia
    heroes_por_caracteristica = {}
    for heroe in lista:
        tipo_caracteristica = heroe[tipo]
        if tipo_caracteristica in heroes_por_caracteristica:
            heroes_por_caracteristica[tipo_caracteristica] += [heroe['nombre']]
        else:
            if tipo_caracteristica == "" or tipo_caracteristica is None:
                tipo_caracteristica = "No tiene"
            heroes_por_caracteristica[tipo_caracteristica] = [heroe['nombre']]

    for tipo_caracteristica, heroes in heroes_por_caracteristica.items():
        print(f"Heroes con {tipo} - {tipo_caracteristica}: ")
        for heroe in heroes:
            print(heroe)


