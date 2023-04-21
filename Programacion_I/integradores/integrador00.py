'''
Desafio Integrador 00
Nombre: Iago Valverde Pachiani
Div - 1D
'''

from data_stark import lista_personajes 
from os import system

def mostrar_nombre_heroes():
    # B - Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
    for heroe in lista_personajes:
        print(f"{heroe['nombre']}")

def mostrar_nombre_altura_heroe():
    # C - Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
    for heroe in lista_personajes:
        print(f"{heroe['nombre']} - {heroe['altura']}")

def mostrar_altura_maxima():
    # D - Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
    flag_maxima_altura = True
    for heroe in lista_personajes:
        heroe['altura'] = float(heroe['altura'])
        if flag_maxima_altura == True or heroe['altura'] > maxima_altura:
            maxima_altura = heroe['altura']
            flag_maxima_altura = False
    print(f"Altura más alta: {maxima_altura}")

def mostrar_altura_minima():
    # E - Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
    flag_minima_altura = True
    for heroe in lista_personajes:
        heroe['altura'] = float(heroe['altura'])
        if flag_minima_altura == True or heroe['altura'] < minima_altura:
            minima_altura = heroe['altura']
            flag_minima_altura = False
    print(f"Altura más baja: {minima_altura}")

def calcular_promedio_altura():
    # F - Recorrer la lista y determinar la altura promedio de los superhéroes (PROMEDIO)
    contador_heroes = len(lista_personajes)
    acumulador_altura = 0
    for heroe in lista_personajes:
        heroe['altura'] = float(heroe['altura'])
        acumulador_altura += heroe['altura']
    promedio_altura = acumulador_altura / contador_heroes
    print(f"Promedio de altura de los heroes: {promedio_altura}")

def mostrar_heroe_altura_maxmin():
    # G - Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
    flag_maxima_altura = True
    for heroe in lista_personajes:
        heroe['altura'] = float(heroe['altura'])
        if flag_maxima_altura == True or heroe['altura'] > maxima_altura:
            maxima_altura = heroe['altura']
            flag_maxima_altura = False
    for heroe in lista_personajes:
        if heroe['altura'] == maxima_altura:
            print(f"Heroe más alto: {heroe['nombre']}")

    flag_minima_altura = True
    for heroe in lista_personajes:
        heroe['altura'] = float(heroe['altura'])
        if flag_minima_altura == True or heroe['altura'] < minima_altura:
            minima_altura = heroe['altura']
            flag_minima_altura = False
    for heroe in lista_personajes:
        if heroe['altura'] == minima_altura:
            print(f"Heroe más bajo: {heroe['nombre']}")

def calcular_peso_maxmin():
    # H - Calcular e informar cual es el superhéroe más y menos pesado.
    flag_peso_maximo = True
    for heroe in lista_personajes:
        heroe['peso'] = float(heroe['peso'])
        if flag_peso_maximo == True or heroe['peso'] > peso_maximo:
            peso_maximo = heroe['peso']
            flag_peso_maximo = False
    print(f"Peso máximo: {peso_maximo}")
    for heroe in lista_personajes:
        if heroe['peso'] == peso_maximo:
            print(f"Heroe más pesado: {heroe['nombre']}")

    flag_peso_minimo = True
    for heroe in lista_personajes:
        heroe['peso'] = float(heroe['peso'])
        if flag_peso_minimo == True or heroe['peso'] < peso_minimo:
            peso_minimo = heroe['peso']
            flag_peso_minimo = False
    print(f"Peso minimo: {peso_minimo}")
    for heroe in lista_personajes:
        if heroe['peso'] == peso_minimo:
            print(f"Heroe menos pesado: {heroe['nombre']}")

menu = ["1. Mostrar nombre de los heroes",
        "2. Mostrar nombre y altura de los heroes", 
        "3. Mostrar altura maxima entre los heroes", 
        "4. Mostrar altura minima entre los heroes", 
        "5. Calcular promedio de las alturas", 
        "6. Mostrar nombre del heroe más alto y del más bajo", 
        "7. Calcular peso máximo y minimo de los heroes", 
        "8. Salir"
]

def mostrar_menu():
    for opcion in menu:
        print(opcion)

while True:
    mostrar_menu()
    respuesta = int(input("Ingrese una opcion: "))
    match respuesta: 
        case 1:
            mostrar_nombre_heroes()
        case 2:
            mostrar_nombre_altura_heroe()
        case 3:
            mostrar_altura_maxima()
        case 4:
            mostrar_altura_minima()
        case 5:
            calcular_promedio_altura()
        case 6:
            mostrar_heroe_altura_maxmin()
        case 7:
            calcular_peso_maxmin()
        case 8:
            break