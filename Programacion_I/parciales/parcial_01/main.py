import csv
import re

# def parser_csv(path:str)->list:
#     personajes = []
#     archivo = open(path, 'r', encoding="ISO-8859-1")    
#     for linea in archivo:
#             personaje = {}
#             personaje['id'] = int(linea[0])
#             personaje['nombre'] = linea[1]
#             personaje['raza'] = linea[2]
#             personaje['poder_pelea'] = linea[3]
#             personaje['poder_ataque'] = linea[4]
#             personaje['habilidades'] = linea[5].split('|%')
#             personajes.append(personaje)
#     archivo.close()

#     return personajes

# def generar_csv(path:str, lista:list):
#     archivo = open(path, 'w', encoding="ISO-8859-1")
#     for i in range(5):
#         registro = "{0},{1},{2},{3},{4},{5}\n"
#         registro = registro.format(personajes[0]['id'],
#                                     personajes[1]['nombre'],
#                                     personajes[2]['raza'],
#                                     personajes[3]['poder_pelea'],
#                                     personajes[4]['poder_ataque'],
#                                     personajes[5]['habilidades'])
#         archivo.write(registro)
#     archivo.close()

# personajes = parser_csv("C:/Users/iagop/Documents/Iago/desenvolvimento-sites/utn-python/Programacion_I/parciales/parcial_01/DBZ.csv")

# generar_csv("archivo_modificado", personajes)
# print(personajes)

def parser_csv(path:str) -> list:
    personajes = []
    with open(path, 'r', encoding="ISO-8859-1") as archivo:
        lector = csv.reader(archivo)
        for linea in lector:
            personaje = {}
            personaje['id'] = int(linea[0])
            personaje['nombre'] = re.sub(" ", "",linea[1])
            personaje['raza'] = re.sub(r'\s+', '', linea[2]).split()
            personaje['poder_pelea'] = int(linea[3])
            personaje['poder_ataque'] = int(linea[4])
            personaje['habilidades'] = re.sub(r'\s+','',linea[5]).split('|$%')
            personajes.append(personaje)
    print(personajes)
    return personajes

parser_csv("C:/Users/iagop/Documents/Iago/desenvolvimento-sites/utn-python/Programacion_I/parciales/parcial_01/DBZ.csv")

def calcular_por_raza(lista:list, tipo_raza:str):
    diccionario_raza = {}
    tipo_raza = personaje['raza']
    for personaje in lista:
        if tipo_raza in diccionario_raza:
            diccionario_raza[tipo_raza] += 1
        else:
            if tipo_raza == "" or tipo_raza is None:
                tipo_raza = "No tiene"
            diccionario_raza[tipo_raza] = 1
    return diccionario_raza

def listar_por_raza(lista):
    with open("C:/Users/iagop/Documents/Iago/desenvolvimento-sites/utn-python/Programacion_I/parciales/parcial_01/DBZ.csv", 'r', encoding="ISO-8859-1") as archivo:
        lector = csv.DictReader(archivo)
        lista = list(lector)
    cantidad_por_raza = calcular_por_raza(lista, 'raza')
    for tipo_raza, cantidad_tipo in cantidad_por_raza.items():
        print(f"Hay {cantidad_tipo} personajes con {tipo_raza}")

listar_por_raza("C:/Users/iagop/Documents/Iago/desenvolvimento-sites/utn-python/Programacion_I/parciales/parcial_01/DBZ.csv")