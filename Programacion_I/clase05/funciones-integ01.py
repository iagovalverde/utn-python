'''
Desafio Integrador 01
Nombre: Iago Valverde Pachiani
Div - 1D
'''

from data_stark import lista_personajes 
from os import system

def mostrar_nombre_heroes():
    # 00B - Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
    for heroe in lista_personajes:
        print(f"{heroe['nombre']}")

def mostrar_nombre_masculino():
    # 01A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
    for heroe in lista_personajes:
        if heroe['genero'] == 'M':
            print(f"{heroe['nombre']}")
            # return {heroe['nombre']}

def mostrar_nombre_femenino():
    # 01B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
    for heroe in lista_personajes:
        if heroe['genero'] == 'F':
            print(f"{heroe['nombre']}")
            # return {heroe['nombre']}

def mostrar_nombre_altura_heroe():
    # 00C - Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
    for heroe in lista_personajes:
        print(f"{heroe['nombre']} - {heroe['altura']}")

def mostrar_altura_maxima():
    # 00D - Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
    flag_maxima_altura = True
    for heroe in lista_personajes:
        heroe['altura'] = float(heroe['altura'])
        if flag_maxima_altura == True or heroe['altura'] > maxima_altura:
            maxima_altura = heroe['altura']
            flag_maxima_altura = False
    print(f"Altura más alta: {maxima_altura}")

def mostrar_maxima_altura_masculino():
    # 01C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
    flag_maxima_altura_m = True
    for heroe in lista_personajes:
        heroe['altura'] = float(heroe['altura'])
        if heroe['genero'] == 'M':
            if flag_maxima_altura_m == True or heroe['altura'] > maxima_altura_m:
                maxima_altura_m = heroe['altura']
                flag_maxima_altura_m = False
    print(f"La altura más alta entre los heroes masculinos: {maxima_altura_m}")

def mostrar_maxima_altura_femenino():
    # 01D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
    flag_maxima_altura_f = True
    for heroe in lista_personajes:
        heroe['altura'] = float(heroe['altura'])
        if heroe['genero'] == 'F':
            if flag_maxima_altura_f == True or heroe['altura'] > maxima_altura_f:
                maxima_altura_f = heroe['altura']
                flag_maxima_altura_f = False
    print(f"La altura más alta entre los heroes femeninos: {maxima_altura_f}")

def mostrar_altura_minima():
    # 00E - Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
    flag_minima_altura = True
    for heroe in lista_personajes:
        heroe['altura'] = float(heroe['altura'])
        if flag_minima_altura == True or heroe['altura'] < minima_altura:
            minima_altura = heroe['altura']
            flag_minima_altura = False
    print(f"Altura más baja: {minima_altura}")

def mostrar_minima_altura_masculino():
    # 01E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
    flag_minima_altura_m = True
    for heroe in lista_personajes:
        heroe['altura'] = float(heroe['altura'])
        if heroe['genero'] == 'M':
            if flag_minima_altura_m == True or heroe['altura'] < minima_altura_m:
                minima_altura_m = heroe['altura']
                flag_minima_altura_m = False
    print(f"La altura más baja entre los heroes masculinos: {minima_altura_m}")

#def mostrar_minima_altura_femenino():
    # 01F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F