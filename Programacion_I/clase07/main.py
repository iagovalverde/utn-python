from data import lista_bzrp
from os import system

{'title': 'QUEVEDO || BZRP Music Sessions #52', 
    'views': 227192970, 
    'length': 204,
    'img_url': 'https://i.ytimg.com/vi/A_g3lMcWVy0/sddefault.jpg',
    'url': 'https://youtube.com/watch?v=A_g3lMcWVy0', 
    'date': '2022-07-06 00:00:00'
}

# Tipo: BZRP MUSIC SESSIONS
# Artista: QUEVEDO
# Numero: 52
# Reproducciones: 227 M
# Duracion: 204 minutos
# Codigo: A_g3lMcWVy0
# Fecha de carga: 6/7/2022
# Hora de carga: 00:00

def prueba():
    titulo = 'QUEVEDO || BZRP Music Sessions #52'
    cadena = titulo.split(" || ")
    artista = cadena[0].strip()
    cadena2 = cadena[1].split("#")
    tipo = cadena2[0].strip()
    numero = cadena2[1].strip()
    print(f"{artista} - {tipo} - {numero}")


def prueba2(titulo:str):
    # titulo = 'QUEVEDO || BZRP Music Sessions #52'
    cadena = titulo.split("||")
    artista = cadena[0].strip()
    cadena2 = cadena[1].split("#")
    tipo = cadena2[0].strip()
    numero = cadena2[1].strip()
    print(f"{artista} - {tipo} - {numero}")

def prueba3(titulo:str):
    # titulo = 'QUEVEDO || BZRP Music Sessions #52'
    cadena = titulo.split("||")
    if(len(cadena) > 1):
        artista = cadena[0].strip()
        cadena2 = cadena[1].split("#")
        if(len(cadena2)> 1):
            tipo = cadena2[0].strip()
            numero = cadena2[1].strip()
            print(f"{artista} - {tipo} - {numero}")

def prueba4(titulo:str):
    tipo = "BZRP Music Sessions"
    parte1 = titulo.split(tipo)
    if(len(parte1) == 2):
        artista = parte1[0].replace("||", "").strip()
        numero = parte1[1].replace("#", "").strip()
        print(f"{artista} - {tipo} - {numero}")

# 'url': 'https://youtube.com/watch?v=A_g3lMcWVy0'
def url(tema:dict):
    #cadena = tema['url'].split("=")
    #print(cadena[1])

    ### otra forma ######
    #codigo = tema['url'].replace("https://youtube.com/watch?v=", "")

    ### otra forma ######
    # l = len("https://youtube.com/watch?v=")
    # url = tema["url"]
    # codigo = url[l:]
    # print(codigo)

    ### otra forma ######
    url = tema["url"]
    indice = url.index("=")
    codigo = url[indice+1:]
    print(codigo)

def test(lista:list):
    for tema in lista:
        url(tema)





def mostrar_lista_temas(lista:list, clave = None, valor = None):
    # B. Recorrer la lista imprimiendo por consola el título de cada video
    if clave is None and valor is None:
        for tema in lista:
            print(f"{tema['title']}")
    else:
        for tema in lista:
            if tema[clave] == valor:
                print(f"{tema['title']}")

def mostrar_lista_temas_views():
    # C. Recorrer la lista imprimiendo por consola el título de cada video junto a la
    # cantidad de reproducciones del mismo
    for tema in lista_bzrp:
        print(f"{tema['title']} - {tema['views']}")

def calcular_maximo(lista:list, clave:str)->int:
    '''
    Brief: Calcula el maximo valor numerico en base a una clave
    Parameters: 
        lista: list -> lista sobre la que voy a hacer la busqueda
        clave: str -> la clave con la cual realizo la busqueda en la lista
    Return: un entero que representa el maximo valor de la clave
    '''
    flag_primero = True
    if(type(lista) == list and len(lista) > 0 and type(clave) == str and clave != ""):

        for tema in lista:
            if flag_primero == True or tema[clave] > maximo:
                maximo = tema[clave]
                flag_primero = False
    
    return maximo

def mostrar_maximo(lista:list, clave: str, valor:int):
    for tema in lista: # buscamos el tema que coincide con el de maxima_views
        if tema[clave] == valor:
            print(f"{tema['title']}")

def mostrar_maximo_reproduciones(lista:list):
    # D. Recorrer la lista y determinar cuál es la cantidad máxima de reproducciones (MÁXIMO)
    maxima_views = calcular_maximo(lista, 'views')
    print(f"Cantidad máxima de reproduccion: {maxima_views}")
    mostrar_lista_temas(lista, 'views', maxima_views)

def buscar_temas_mas_largos(lista:list):
    maximo_len = calcular_maximo(lista, 'length')
    print(f"Duracion maximo: {maximo_len}")
    mostrar_lista_temas(lista, 'length', maximo_len)

def mostrar_minimo_reproduciones():
    # E. Recorrer la lista y determinar cuál es la cantidad mínima de reproducciones (MÍNIMO)
    flag_primero = True
    for tema in lista_bzrp:
        if flag_primero == True or tema['views'] < minima_views:
            minima_views = tema['views']
            flag_primero = False
    print(f"Cantidad minima de reproduccion: {minima_views}")
    for tema in lista_bzrp: # buscamos el tema que coincide con el de minima_views
        if tema['views'] == minima_views:
            print(f"{tema['title']}")

def calcular_promedio():
    # F. Recorrer la lista y determinar la cantidad total de reproducciones del canal(ACUMULADOR)
    # G. Recorrer la lista y determinar la cantidad promedio de reproducciones que
    # tiene un video (PROMEDIO)
    acumulador_views = 0
    for tema in lista_bzrp:
        acumulador_views += tema['views']
    print(f"Sumatoria de views: {acumulador_views}")
    contador_temas = len(lista_bzrp)
    promedio_views = acumulador_views / contador_temas
    print(f"El promedio de views es: {promedio_views}")

# K. Construir un menú que permita elegir qué dato obtener

menu = ["1. Mostrar temas", 
        "2. Mostrar temas con las views", 
        "3. Mostrar temas con mas views", 
        "4. Mostrar temas con menos views", 
        "5. Mostrar el promedio de views", 
        "6. Salir"]

def mostrar_menu():
    for opcion in menu:
        print(opcion)

system("cls")
while True:
    mostrar_menu()
    respuesta = int(input("Ingrese una opcion: "))
    match respuesta:
        case 1:
            mostrar_lista_temas(lista_bzrp)
        case 2:
            buscar_temas_mas_largos(lista_bzrp)
        case 3:
            mostrar_maximo_reproduciones(lista_bzrp)
        case 4:
            mostrar_minimo_reproduciones()
        case 5:
            calcular_promedio()
        case 6:
            break
        case 7:
            test(lista_bzrp)

