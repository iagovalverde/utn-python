from data_stark import lista_personajes 
from os import system

system("cls")

# B - Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
for heroe in lista_personajes:
    print(f"{heroe['nombre']}")

# C - Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo

for heroe in lista_personajes:
    print(f"{heroe['nombre']} - {heroe['altura']}")

# D - Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
flag_mas_alto = True

for heroe in lista_personajes:
    if flag_mas_alto == True or float(heroe['altura']) > mas_alto:
        mas_alto = float(heroe['altura'])
        flag_mas_alto = False
print(f"Altura más alta: {mas_alto}")

for heroe in lista_personajes:
    if heroe['altura'] == mas_alto:
        print(f"El heroe más alto: {float(heroe['nombre'])}")

# E - Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
flag_mas_bajo = True

for heroe in lista_personajes:
    if flag_mas_bajo == True or heroe['altura'] < mas_bajo:
        mas_bajo = heroe['altura']
        flag_mas_bajo = False
print(f"Altura más baja: {mas_bajo}")

for heroe in lista_personajes:
    if heroe['altura'] == mas_bajo:
        print(f"El heroe más bajo: {heroe['nombre']}")

# F - Recorrer la lista y determinar la altura promedio de los superhéroes (PROMEDIO)

contador_heroes = len(lista_personajes)
acumulador_altura = 0

for heroe in lista_personajes:
    acumulador_altura += heroe['altura']

promedio_altura = acumulador_altura / contador_heroes
print(f"El promedio de altura de los heroes: {promedio_altura}")
