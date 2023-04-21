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
                heroe_mas_alto = heroe['nombre']
                flag_maxima_altura = False
        else:
            if genero == None:
                if flag_maxima_altura == True or heroe['altura'] > maxima_altura:
                    maxima_altura = heroe['altura']
                    heroe_mas_alto = heroe['nombre']
                    flag_maxima_altura = False
    print(f"Heroe más alto: {heroe_mas_alto} - Altura maxima {maxima_altura}")

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
                heroe_mas_bajo = heroe['nombre']
                flag_minima_altura = False
        else:
            if genero == None:
                if flag_minima_altura == True or heroe['altura'] < minima_altura:
                    minima_altura = heroe['altura']
                    heroe_mas_bajo = heroe['nombre']
                    flag_minima_altura = False
    print(f"Heroe más bajo: {heroe_mas_bajo} - Altura minima {minima_altura}")

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

