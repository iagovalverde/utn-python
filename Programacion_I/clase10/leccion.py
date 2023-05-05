# Dos tipo de texto: texto y binarios
'''
La diferencia es la forma en 
que se interpretan a la forma de escribirse o leerse, 
en que se codifica.

Archivos txt: archivos de texto plano
Archivos CSV: Especiales que permiten guardar datos separados por coma o punto y coma.
Archivos binarios: Permite guardar una secuencia de numeros binarios 
segun el tipo de dato que estoy guardando.
'''

# Archivos:

'''
CSV: documento que representa los datos como tabla, organizando en filas y columnas.
las columnas se separan con (;)
'''

#Modo de apertura:

'''
* r = abre un texto solo para lectura
rb = are un texto binario solo para leer
* r+ = abre un archivo de texto para leer y escribir(si existe, lo sobreescribe)
* w = abre un archivo de texto solo para escritura (si existe, lo sobreescribe)
wb = abre un archivo binario solo para escritura (si existe, lo sobreescribe)
* w+ = abre un archivo para escritura y lectura (si existe lo sobreescribe)
* a = abre un archivo y anexa informacion
x = crea un archivo para escribir sobre él

* marcados porque estan propensos a usarse este cuatrimestre
'''

#Archivos JSON

'''
El nombre viene de JavaScript Object Notation
Es de facil lectura.

'''

#Codigo

'''
* Para abrir un archivo, función open:
archivo = open(nombre_archivo, modo)
Open recibe dos parámetros.
archivo: objeto file, se va a usar para llamar otros 
metodos asociados al archivo
nombre_archivo: string que contiene el nombre del archivo
modo: string que contiene el modo de apertura

* Para cerrar un archivo:
archivo.close()

* Objeto file: permite obtener además de los datos del archivo, el nombre del archivo, directorio, etc

archivo.closed: retorna True si esta cerrado o False en el caso contrario
archivo.mode: retorna el modo de apertura
archivo.name: retorna el nombre del archivo

* Para leer un archivo:
archivo.read()

* Para escribir un archivo:
archivo.write()

* Para abrir el archivo y que este, luego de realizar la accion,
se cierre por si solo:
with open("archivo.txt", "r+") as archivo:
    for linea in archivo:
        print(linea, end="")
'''
#TEXTO

mi_archivo = open("nombre.txt","w") # si no existe, lo crea
mi_archivo.write("pajaritos\n")
mi_archivo.close()

mi_archivo = open("nombre.txt", "a")
mi_archivo.write("perritos\n")
mi_archivo.close()

mi_archivo = open("nombre.txt", "a", encoding="utf-8")
mi_archivo.write("gatitos\n")
mi_archivo.close()

mi_archivo = open("nombre.txt")
registro = mi_archivo.read() #lee todo
mi_archivo.close()
print(registro)

mi_archivo = open("nombre.txt")
registro = mi_archivo.readline() # lee una linea sola (primera, a menos que especifiquemos)
mi_archivo.close()
print(registro)

lista = ["Thiago", "Gio", "Marian", "Mario"]

with open("lista_nombres.txt","w") as mi_archivo:
    for line in lista:
        mi_archivo.write(f"{line}\n")

mi_archivo = open("lista_nombres.txt","r")
lista = mi_archivo.read() #Lee el archivo
print(lista)

mi_archivo = open("lista_nombres.txt","r")
lista = mi_archivo.readlines() #Devuelve una lista, incluyendo a los saltos de linea
print(lista)

mi_archivo = open("lista_nombres.txt","r")
lista = mi_archivo.readlines() 
for line in lista:
    print(line,end="") #Suprime los espacios de más, por tener los saltos de linea

with open("lista_nombres.txt","r") as mi_archivo:
    for line in mi_archivo:
        print(line, end="")

## CSV

nombres = ["Thiago", "Gio", "Marian"] #variable global
apellidos = ["Mejias", "Luchetta", "Fernandez"]
edades = [21,23,24]
TAM = 3
with open("agenda.csv","w") as archivo:
    for i in range(TAM):
        registro ="{0},{1},{2}\n".format(nombres[i],apellidos[i],edades[i]) #variable local
        archivo.write(registro)

import re
with open("agenda.csv","r") as archivo:
    for line in archivo:
        # registro = line.split(",")
        registro = re.split(r",|\n", line)
        print(f"{registro[0]} - {registro[1]} - {registro[2]}")

##JSON
# import json

# data = {}
# data["alumnos"] = []
# data["alumnos"].append({"nombre":"juan", "edad":20})
# data["alumnos"].append({"nombre":"luis", "edad":24})
# data["alumnos"].append({"nombre":"pepe", "edad":19})

# with open("agenda.json", "w") as mi_archivo:
#     json.dump(data, mi_archivo, indent = 4)

# with open("agenda.json","r") as mi_archivo:
#     data = json.load(mi_archivo)

