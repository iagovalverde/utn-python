'''
Realizar una carga indefinida de números, añadirlos a una lista e indicar que posición
de memoria es la que mas ocurrencias tiene dentro de esa lista.
'''

lista_numeros = []

while True:
    entrada_numero = input("Ingrese un numero [deje vacío para salir]: ")
    if entrada_numero == "":
        break
    lista_numeros.append(int(entrada_numero))

for numero in lista_numeros:
    print(f"{numero}...", end = "")
