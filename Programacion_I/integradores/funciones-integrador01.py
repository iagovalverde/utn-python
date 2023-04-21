'''
Desafio Integrador 01
Nombre: Iago Valverde Pachiani
Div - 1D
'''

from data_stark import lista_personajes 
from os import system

def mostrar_nombre_heroes(genero):
    # A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
    # B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F

    for heroe in lista_personajes:
        if heroe['genero'] == genero:
            print(heroe['nombre'])
        else:
            if genero == None:
                print(heroe['nombre'])

#mostrar_nombre_heroes('M')

def mostrar_maxima_altura_heroes(genero):
    # C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
    # D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F

    flag_maxima_altura = True
    for heroe in lista_personajes:
        heroe['altura'] = float(heroe['altura'])
        if heroe['genero'] == genero:
            if flag_maxima_altura == True or heroe['altura'] > maxima_altura:
                maxima_altura = heroe['altura']
                flag_maxima_altura = False
        else:
            if genero == None:
                if flag_maxima_altura == True or heroe['altura'] > maxima_altura:
                    maxima_altura = heroe['altura']
                    flag_maxima_altura = False
    print(f"Altura maxima: {maxima_altura}")

# mostrar_maxima_altura_heroes(None)

def mostrar_minima_altura_heroes(genero):
    # E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
    # F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F

    flag_minima_altura = True
    for heroe in lista_personajes:
        heroe['altura'] = float(heroe['altura'])
        if heroe['genero'] == genero:
            if flag_minima_altura == True or heroe['altura'] < minima_altura:
                minima_altura = heroe['altura']
                flag_minima_altura = False
        else:
            if genero == None:
                if flag_minima_altura == True or heroe['altura'] < minima_altura:
                    minima_altura = heroe['altura']
                    flag_minima_altura = False
    print(f"Altura minima: {minima_altura}")

# mostrar_minima_altura_heroes('F')

def calcular_promedio_altura(genero):
    # G. Recorrer la lista y determinar la altura promedio de los superhéroes de género M
    # H. Recorrer la lista y determinar la altura promedio de los superhéroes de género F
    
    acumulador_altura = 0
    contador_heroes = 0
    for heroe in lista_personajes:
        heroe['altura'] = float(heroe['altura'])
        if heroe['genero'] == genero:
            acumulador_altura += heroe['altura']
            contador_heroes += 1
        else:
            if genero == None:
                acumulador_altura += heroe['altura']
                contador_heroes = len(lista_personajes)
    promedio_altura = acumulador_altura / contador_heroes
    print(f"Promedio de altura de los heroes: {promedio_altura}")

# calcular_promedio_altura(None)

# I. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)

def calcular_color_ojos():
    # J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
    diccionario_ojos = {}
    for heroe in lista_personajes:
        tipo_ojo = heroe['color_ojos']
        if tipo_ojo in diccionario_ojos:
            diccionario_ojos[tipo_ojo] += 1
        else:
            diccionario_ojos[tipo_ojo] = 1
    
    for tipo_ojo, cantidad in diccionario_ojos.items():
        print(f"Hay {cantidad} heroes con ojos de color {tipo_ojo}")
    print(diccionario_ojos)
# calcular_color_ojos()

def calcular_color_pelo():
    # K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
    diccionario_pelo = {}
    for heroe in lista_personajes:
        tipo_pelo = heroe['color_pelo']
        if tipo_pelo in diccionario_pelo:
            diccionario_pelo[tipo_pelo] += 1
        else:
            diccionario_pelo[tipo_pelo] = 1

    for tipo_pelo, cantidad in diccionario_pelo.items():
        print(f"Hay {cantidad} heroes con ojos de color {tipo_pelo}")
# calcular_color_pelo()

def calcular_tipo_inteligencia():
    # L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ('No Tiene').
    diccionario_inteligencia = {}
    for heroe in lista_personajes:
        tipo_inteligencia = heroe['inteligencia']
        if tipo_inteligencia in diccionario_inteligencia:
            diccionario_inteligencia[tipo_inteligencia] += 1
        else:
            if tipo_inteligencia == "" or tipo_inteligencia is None:
                tipo_inteligencia = "No tiene"
            diccionario_inteligencia[tipo_inteligencia] = 1
    
    for tipo_inteligencia, cantidad in diccionario_inteligencia.items():
        print(f"Hay {cantidad} in heroes con inteligencia - {tipo_inteligencia}")
# calcular_tipo_inteligencia()

def listar_heroes_color_ojos():
    # M. Listar todos los superhéroes agrupados por color de ojos.
    heroes_por_color_ojos = {}
    for heroe in lista_personajes:
        tipo_ojo = heroe['color_ojos']
        if tipo_ojo in heroes_por_color_ojos:
            heroes_por_color_ojos[tipo_ojo] += [heroe['nombre']]
        else:
            heroes_por_color_ojos[tipo_ojo] = [heroe['nombre']]

    for tipo_ojo, heroes in heroes_por_color_ojos.items():
        print(f"Heroes con ojos {tipo_ojo}: ")
        for heroe in heroes:
            print(heroe)

#listar_heroes_color_ojos()

def listar_heroes_color_pelo():
    # N. Listar todos los superhéroes agrupados por color de pelo.
    heroes_por_color_pelo = {}
    for heroe in lista_personajes:
        tipo_pelo = heroe['color_pelo']
        if tipo_pelo in heroes_por_color_pelo:
            heroes_por_color_pelo[tipo_pelo] += [heroe['nombre']]
        else:
            if tipo_pelo == "" or tipo_pelo is None:
                tipo_pelo = "Sin pelo"
            heroes_por_color_pelo[tipo_pelo] = [heroe['nombre']]

    for tipo_pelo, heroes in heroes_por_color_pelo.items():
        print(f"Heroes con pelo - {tipo_pelo}: ")
        for heroe in heroes:
            print(heroe)

listar_heroes_color_pelo()

def listar_heroes_inteligencia():
    heroes_por_tipo_inteligencia = {}
    for heroe in lista_personajes:
        tipo_inteligencia = heroe['inteligencia']
        if tipo_inteligencia in heroes_por_tipo_inteligencia:
            heroes_por_tipo_inteligencia[tipo_inteligencia] += [heroe['nombre']]
        else:
            if tipo_inteligencia == "" or tipo_inteligencia is None:
                tipo_inteligencia = "Nula"
            heroes_por_tipo_inteligencia[tipo_inteligencia] = [heroe['nombre']]
    
    for tipo_inteligencia, heroes in heroes_por_tipo_inteligencia.items():
        print(f"Heroes con tipo inteligencia - {tipo_inteligencia}: ")
        for heroe in heroes:
            print(heroe)

listar_heroes_inteligencia()

