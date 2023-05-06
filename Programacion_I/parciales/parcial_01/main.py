import csv
import re

personajes = []

with open("C:/Users/iagop/Documents/Iago/desenvolvimento-sites/utn-python/Programacion_I/parciales/parcial_01/DBZ.csv", "r", encoding="ISO-8859-1") as archivo:
    arquivo_csv = csv.reader(archivo, delimiter=",")
    for linea in arquivo_csv:
        personaje = {
            'id': linea[0],
            'nombre': linea[1],
            'raza': re.split(",", linea[2]),
            'poder_de_pelea': linea[3],
            'poder_de_ataque': linea[4],
            'habilidades': re.split(",", linea[5])
        }
        personajes.append(personaje)


print(personajes)

# with open("C:/Users/iagop/Documents/Iago/desenvolvimento-sites/utn-python/Programacion_I/parciales/parcial_01/DBZ.csv", "r", encoding='ISO-8859-1') as archivo:
#     arquivo_csv = csv.reader(archivo, delimiter=",")
#     for linha in arquivo_csv:
#         print(linha)