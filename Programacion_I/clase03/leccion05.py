#LISTAS#

#Definir y agregar elementos por extension y por metodo append
mi_lista = []

mi_lista.append(4) # 0
mi_lista.append(5) # 1
mi_lista.append(2) # 2
mi_lista.append(6) # 3

print(mi_lista)

#Recordar listas por indice y por elementos

# for i in range(len(mi_lista)):
#    print(mi_lista[i])

for numero in mi_lista:
    print(numero)


#Eliminar elementos de una lista

mi_lista.remove(2)

#TUPLAS#    es una lista inmutable

mi_tupla = (3,6,9,7)

print(type(mi_tupla))

#SET#   desordena el orden y elimina los que se repiten

mi_set = {5,5,7,6,9,2}  #set([5,6,9,5,7,4,5,3])

print(mi_set)

#DICCIONARIOS#

mi_diccionario = {}   #{"codigo": 5, "descripcion": "Coca Cola"}
mi_diccionario["codigo"] = 5
mi_diccionario["descripcion"] = "Coca Cola"
mi_diccionario["precio"] = 33.65
#print(mi_diccionario["codigo"])
for clave in mi_diccionario:  # ver la clave
    print(clave)

for clave in mi_diccionario:  # ver claves con sus valores
    print(f"{clave}: {mi_diccionario[clave]}")

#Definicion de un diccionario por extension

#Definir un diccionario y agregar claves y valores

#Obtener claves

#Obtener valores

#LISTAS de DICCIONARIOS#

lista_productos = []

producto1 = {"codigo": 5, "descripcion": "Coca cola", "precio": 400}
producto2 = {"codigo": 3, "descripcion": "Pepsi", "precio": 350}
producto3 = {"codigo": 9, "descripcion": "Fanta", "precio": 450}

lista_productos.append(producto1)
lista_productos.append(producto2)
lista_productos.append(producto3)

print(lista_productos)

#Otra forma de crear lo de arriba

lista_productos = []
CANTIDAD = 3
for i in range(CANTIDAD):
    codigo = int(input("Ingrese el codigo: "))
    descripcion = input("Ingrese descripcion: ")
    precio = float(input("Ingrese el precio: "))
    un_producto = {}
    un_producto["codigo"] = codigo
    un_producto["descripcion"] = descripcion
    un_producto["precio"] = precio
    lista_productos.append(un_producto)

    for producto in lista_productos:
        print(f"{producto['codigo']}--{producto['descripcion']}--{producto['precio']}")

print(lista_productos)

#Crear la lista y cargar elementos


#Recorrer la lista y mostrar los elementos

lista_productos = []
CANTIDAD = 3
for i in range(CANTIDAD):
    codigo = int(input("Ingrese el codigo: "))
    descripcion = input("Ingrese descripcion: ")
    precio = float(input("Ingrese el precio: "))
    un_producto = {}
    un_producto["codigo"] = codigo
    un_producto["descripcion"] = descripcion
    un_producto["precio"] = precio
    lista_productos.append(un_producto)

    for producto in lista_productos:
        print(f"{producto['codigo']}--{producto['descripcion']}--{producto['precio']}")

print(lista_productos)