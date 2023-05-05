# TEXTO

# mi_archivo = open("nombre.txt", "a", encoding = "UTF-8")
# mi_archivo.write("rampi")
# mi_archivo.close()

### PARA LEER UNA LINEA TRAS OTRA

# mi_archivo = open("nombre.txt")
# registro = mi_archivo.readline()
# print(registro)
# registro = mi_archivo.readline()
# print(registro)
# registro = mi_archivo.readline()
# print(registro)
# mi_archivo.close()

### PARA ESCRIBIR SALTANDO LINEA \n

# mi_archivo = open("nombre.txt", "a", encoding = "UTF-8")
# mi_archivo.write("mario\n")
# mi_archivo.close()

# lista = ['Thiago', 'Gio', 'Marian', 'Mario']
# with open("lista_nombres.txt", "w") as mi_archivo:
#     for nombre in lista:
#         mi_archivo.write(f"{nombre}\n")


# mi_archivo = open("lista_nombres.txt", "r")
# lista = mi_archivo.readlines()
# for line in lista:
#     print(line,end="")


# with open("lista_nombres.txt", "r") as mi_archivo:
#     for line in mi_archivo:
#         print(line, end="")


### CSV 

# nombres = ["Thiago", "Gio", "Marian"]
# apellidos = ["Mejias", "Lucchetta", "Fernandez"]
# edades = [21, 23, 24]
# TAM = 3

# with open("agenda.csv", "w") as archivo:
#     for i in range(3):
#         registro = "{0},{1},{2}\n".format(nombres[i], apellidos[i], edades[i])
#         archivo.write(registro)
# import re
# with open("agenda.csv", "r") as archivo:
#     for line in archivo:
#         #registro = line.split(",")
#         registro = re.split(r",|\n", line)
#         print(f"{registro[0]} - {registro[1]} - {registro[2]}")


### JSON

import json

# data = {}
# data["alumnos"] = []
# data["alumnos"].append({"nombre":"Juan", "edad":20})
# data["alumnos"].append({"nombre":"Luis", "edad":29})
# data["alumnos"].append({"nombre":"Maria", "edad":32})

# with open("agenda.json", "w") as mi_archivo:
#     json.dump(data, mi_archivo, indent= 4)

# with open("agenda.json", "r") as mi_archivo:
#     data = json.load(mi_archivo)

# print(data)



import re

def parser_csv(path:str)->list:
    lista = []

    archivo = open(path, "r", encoding= "utf-8")
    for line in archivo:
        lectura = re.split(",|\n", line)
        tema = {}
        tema["title"] = lectura[0]
        tema["views"] = int(lectura[1])
        tema["length"] = int(lectura[2])
        tema["img_url"] = lectura[3]
        tema["url"] = lectura[4]
        tema["date"] = lectura[5]
        lista.append(tema)
    archivo.close()

    return lista

def generar_csv(path:str, lista:list):
    archivo = open(path, "w", encoding="utf-8")
    for i in range(5):
        registro = "{0},{1},{2},{3},{4},{5}\n"
        registro = registro.format(lista[i]["title"], 
                                   lista[i]["views"],
                                   lista[i]['length'],
                                   lista[i]['img_url'],
                                   lista[i]['url'],
                                   lista[i]['date'])
        archivo.write(registro)
    archivo.close()

lista = parser_csv("data.csv")

generar_csv("lista_modificada", lista)
print(lista)
