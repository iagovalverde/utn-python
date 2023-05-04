'''
Desafio Integrador 03
Nombre: Iago Valverde Pachiani
Div - 1D
'''

import re
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
    return codigo

# 2.2
def agregar_codigo_heroe(heroe:dict, id_heroe:int):
    if len(heroe) == 0:
        return False
    heroe['codigo_heroe'] = generar_codigo_heroe(id_heroe, heroe['genero'])
    if len(heroe['codigo_heroe']) != 10:
        return False
    return True

# 2.3 
def stark_generar_codigos_heroes(lista_heroes:list):
    if len(lista_heroes) == 0:
        print("El origen de datos no contiene el formato correcto")
    for heroe in lista_heroes:
        if not isinstance(heroe, dict) or 'genero' not in heroe:
            print("El origen de datos no contiene el formato correcto")
        for i in range(len(lista_heroes)):
            heroe = lista_heroes[i]
            id_heroe = i + 1
            agregar_codigo_heroe(heroe, id_heroe)

    print(f"Se asignaron {len(lista_heroes)} códigos"
        f"\n* El código del primer héroe es: {lista_heroes[0]['codigo_heroe']}"
        f"\n* El código del último héroe es: {lista_heroes[-1]['codigo_heroe']}")
    


# 3.1
def sanitizar_entero(numero_str:str):
    numero_str = numero_str.strip()

    if not numero_str.isdigit():
        return -1
    
    numero_int = int(numero_str)
    if numero_int < 0:
        return -2
    if isinstance(numero_int, int):
        return numero_int
    else:
        return -3

# 3.2 
def sanitizar_flotante(numero_str:str):
    numero_str = numero_str.strip()

    if not numero_str.isdigit():
        return -1
    
    numero_float = float(numero_str)
    if numero_float < 0:
        return -2
    if isinstance(numero_float, float):
        return numero_float
    else:
        return -3

# 3.3
def sanitizar_string(valor_str:str, valor_por_defecto:str = '-'):
    valor_str = valor_str.strip()
    valor_por_defecto = valor_por_defecto.strip()

    if "/" in valor_str:
        valor_str.replace("/", " ")
    
    if not valor_str.isalpha():
        return "N/A"
    else:
        if len(valor_str) == 0:
            return valor_por_defecto.lower()
        else:
            return valor_str.lower()

# 3.4
def sanitizar_dato(heroe:dict, clave:str, tipo_dato:str):
    tipo_dato = tipo_dato.lower()

    if tipo_dato not in ['string', 'entero', 'flotante']:
        print("Tipo de dato no reconocido")
        return False
    
    if clave not in heroe:
        print("La clave especificada no existe en el héroe")
        return False

    valor = heroe[clave]
    if tipo_dato == 'string':
        valor = sanitizar_string(valor)
    else:
        if tipo_dato == 'entero':
            valor = sanitizar_entero(valor)
        else:
            if tipo_dato == 'flotante':
                valor = sanitizar_flotante(valor)

    sanitizado = False
    if valor != heroe[clave]:
        heroe[clave] = valor
        sanitizado = True

    return sanitizado

# 3.5
def generar_indice_nombres(lista_heroes:list):
    if len(lista_heroes) == 0:
        print("Error: Lista de héroes vacía")

    for heroe in lista_heroes:
        for clave in ['altura', 'peso', 'color_ojos', 'color_pelo', 'fuerza', 'inteligencia']:
            tipo_dato = 'string'
            if clave in ['altura', 'peso', 'fuerza']:
                tipo_dato = 'flotante'

        sanitizado = sanitizar_dato(heroe, clave, tipo_dato)
        if sanitizado == True:
            print("Datos normalizados")

generar_indice_nombres(lista_personajes)

# 4.1
def generar_indice_nombres(lista_heroes:list):
    if len(lista_heroes) == 0:
        print("El origen de datos no contiene el formato correcto")
    lista_split = []    
    for heroe in lista_heroes:
        if not isinstance(heroe, dict) or 'nombre' not in heroe:
            print("El origen de datos no contiene el formato correcto")
    
        nombre = (heroe['nombre'])
        nombre_split = re.split(" |-", nombre)
        lista_split += nombre_split
    return lista_split

# 4.2
def stark_imprimir_indice_nombre(lista_heroes:list):
    nombres_split = generar_indice_nombres(lista_heroes)
    nombres_split = str(nombres_split)
    #print(nombres_split)
    print(re.sub("', '", "-", nombres_split))
    

stark_imprimir_indice_nombre(lista_personajes)