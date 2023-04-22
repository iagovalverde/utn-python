from data import lista_bzrp
from os import system

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










# print(type(lista_bzrp))
# print(type(lista_bzrp[0]))

# B. Recorrer la lista imprimiendo por consola el título de cada vídeo

for tema in lista_bzrp:
    print(f"{tema['title']}")
# ----------------------------------
for i in range(len(lista_bzrp)):
    print(f"{lista_bzrp[i]['title']}")

# C. Recorrer la lista imprimiendo por consola el título de cada video junto a la
# cantidad de reproducciones del mismo

for tema in lista_bzrp:
    print(f"{tema['title']} - {tema['views']}")

# D. Recorrer la lista y determinar cuál es la cantidad máxima de reproducciones (MÁXIMO)

flag_primero = True
# maxima_views = lista_bzrp[0]["views"]   # recorrer la lista y buscar las views del indice 0

for tema in lista_bzrp:
    if flag_primero == True or tema['views'] > maxima_views:
        maxima_views = tema['views']
        flag_primero = False

print(f"Cantidad máxima de reproduccion: {maxima_views}")

for tema in lista_bzrp: # buscamos el tema que coincide con el de maxima_views
    if tema['views'] == maxima_views:
        print(f"{tema['title']}")

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

# F. Recorrer la lista y determinar la cantidad total de reproducciones del canal (ACUMULADOR)

acumulador_views = 0

for tema in lista_bzrp:
    acumulador_views += tema['views']

print(f"Sumatoria de views: {acumulador_views}")

# G. Recorrer la lista y determinar la cantidad promedio de reproducciones que
# tiene un video (PROMEDIO)

contador_temas = len(lista_bzrp)

#for tema in lista_bzrp:
#    contador_temas += 1

promedio_views = acumulador_views / contador_temas

print(f"El promedio de views es: {promedio_views}")

# H. Informar cual es el Título del vídeo asociado a cada uno de los indicadores
# anteriores (MÁXIMO, MÍNIMO, ACUMULADOR y PROMEDIO)


# I. Calcular e informar cual es el video que más y el que menos dura.


# J. Ordenar el código implementando una función para cada uno de los valores informados
