'''
Desafio Integrador 03
Nombre: Iago Valverde Pachiani
Div - 1D
'''

from data_stark import lista_personajes
from os import system

# 1.1
def extraer_iniciales(nombre_heroe:str):
    if nombre_heroe == "":
        return 'N/A'
    if 'the' in nombre_heroe:
        nombre_heroe = nombre_heroe.replace("the ", "")
    if '-' in nombre_heroe:
        nombre_heroe = nombre_heroe.replace("-", " ")

    nombres = nombre_heroe.split()
    iniciales = []
    for palabra in nombres:
        iniciales += palabra[0]

    iniciales = '.'.join(iniciales)
    iniciales += '.'
    return iniciales


# 1.2
def definir_iniciales_nombre(heroe:dict):
    if not isinstance(heroe, dict) or 'nombre' not in heroe:
        return False

    heroe['iniciales'] = extraer_iniciales(heroe['nombre'])
    return True

# 1.3
def agregar_iniciales_nombre(lista_heroes:list):
    if not isinstance(lista_heroes, list) or len(lista_heroes) == 0:
        return False
    
    for heroe in lista_heroes:
        if definir_iniciales_nombre(heroe) == False:
            print("El origen de datos no contiene el formato correcto")
            return False
    return True

# 1.4
def stark_imprimir_nombres_con_iniciales(lista_heroes: list):
    if not isinstance(lista_heroes, list) or len(lista_heroes) == 0:
        return 
    
    if agregar_iniciales_nombre(lista_heroes) == True:
        for heroe in lista_heroes:
            if 'iniciales' in heroe:
                iniciales = heroe['iniciales']
                print(f"* {heroe['nombre']} ({iniciales})")

# 2.1
def generar_codigo_heroe(id_heroe: int, genero_heroe:str):
    if not isinstance(id_heroe, int):
        return 'N/A'
    if genero_heroe not in ['M', 'F', 'NB'] or len(genero_heroe) == "":
        return 'N/A'
    
    codigo = f"{genero_heroe}-{str(id_heroe).zfill(10 - len(genero_heroe))}"
    print(codigo)

generar_codigo_heroe(43323550, 'M')

# 2.2
#def agregar_codigo_heroe(heroe:dict, id_heroe:int):

