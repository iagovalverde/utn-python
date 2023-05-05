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



# 4.1
def generar_indice_nombres(lista_heroes:list):
    if len(lista_heroes) == 0:
        print("El origen de datos no contiene el formato correcto")
    lista_split = []    
    for heroe in lista_heroes:
        if not isinstance(heroe, dict) or 'nombre' not in heroe:
            print("El origen de datos no contiene el formato correcto")
    
        nombre_split = re.split(" |-", heroe['nombre'])
        lista_split += nombre_split
    return lista_split

# 4.2
def stark_imprimir_indice_nombre(lista_heroes:list):
    nombres_split = generar_indice_nombres(lista_heroes)
    nombres_split = str(nombres_split)
    nombres_split = re.sub("\['|'\]", "", nombres_split)
    print(re.sub("', '", "-", nombres_split))


# 5.1
def convertir_cm_a_mtrs(valor_cm:float):
    if not isinstance(valor_cm, float) or valor_cm < 0:
        return -1
    
    valor_mtrs = valor_cm / 100

    return valor_mtrs

# 5.2
def generar_separador(patron:str, largo:int, imprimir:bool = True):
    if not isinstance(patron, str) or len(patron) < 1 or len(patron) > 2:
        return "N/A"
    if not isinstance(largo, int) or largo < 1 or largo > 235:
        return "N/A"
    
    separador = patron * largo
    if imprimir == True:
        print(separador)
    else:
        return separador

generar_separador('*',10)

# 5.3 
def generar_encabezado(titulo:str):
    largo_separador = 100
    separador = '*' * largo_separador
    titulo_mayuscula = titulo.upper()
    encabezado = f"{separador}\n{titulo_mayuscula}\n{separador}"

    return encabezado

# 5.4
def imprimir_ficha_heroe(heroe:dict):
    titulo_principal = generar_encabezado('principal')
    titulo_fisico = generar_encabezado('fisico')
    titulo_señas_particulares = generar_encabezado('señas particulares')

    nombre: stark_imprimir_nombres_con_iniciales(heroe)
    

    ficha_heroe = (f"{titulo_principal}\nNOMBRE DEL HÉROE: {heroe['nombre']}")
    
    # f"\nIDENTIDAD SECRETA: {heroe['identidad']}"
    # f"\nCONSULTORA: {heroe['empresa']}"
    # #f"\nCÓDIGO DE HÉROE: {heroe}" #######
    # f"\n{titulo_fisico}"
    # f"\nALTURA: {heroe['altura']}"
    # f"\nPESO: {heroe['peso']}"
    # f"\nFUERZA: {heroe['fuerza']}"
    # f"\n{titulo_señas_particulares}"
    # f"\nCOLOR DE OJOS: {heroe['color_ojos']}"
    # f"\nCOLOR DE PELO: {heroe['color_pelo']}"

    print(ficha_heroe)

imprimir_ficha_heroe()

# 5.5
def stark_navegar_fichas(lista_heroes:list):
    posicion = 1

    while True:
        ficha = imprimir_ficha_heroe(lista_heroes[posicion])
        print(ficha)

        opcion = int(input("[1] Ir a la izquierda [2] Ir a la derecha [S] Salir"))
        match opcion:
            case 1:
                posicion = (posicion - 1)
            case 2: 
                posicion = (posicion + 1)
            case 3:
                break
            case _: 
                pass

#stark_navegar_fichas(lista_personajes)