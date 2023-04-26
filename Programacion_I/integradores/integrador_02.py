from data_stark import lista_personajes
from funciones_02 import *
from os import system

stark_normalizar_datos(lista_personajes,'fuerza')

for heroe in lista_personajes:
    print(heroe['altura'])
