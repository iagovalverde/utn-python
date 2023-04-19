'''
La real academia española nos pide desarrollar un pequeño programa que contenta el
diccionario de la lengua española y su traducción al inglés. Para esto necesitamos un
algoritmo que nos permita el ingreso de una palabra en español y su traducción al
ingles y guardarlo en una lista. Si la palabra no existe, debemos agregarla, y si la
palabra existe debemos informar que la palabra ya existe y su índice dentro del listado,
esta carga debe ser hasta que el usuario se canse de ingresar palabras. Al finalizar se
debe mostrar todo el listado de palabras ingresadas con su palabra equivalente en
inglés. Recordar validar los datos de forma correcta.
'''

lista_palabras = []
respuesta = "si"

while respuesta == "si":
    palabra_espanol = input("Ingrese una palabra en español: ")
    palabra_repetida = False

    for i in range(len(lista_palabras)):
        if palabra_espanol in lista_palabras[i]["Palabra Española"]:
            palabra_repetida = True
            break

    if palabra_repetida == True:
        print("La palabra ya existe")
    else:
        palabra_ingles = input("Ingrese la traduccion al inglés: ")
        diccionario_palabras = {
            "Palabra Española" : palabra_espanol, 
            "Traducion" : palabra_ingles
        }
        lista_palabras.append(diccionario_palabras)

    respuesta = input("Ingresas más palabras? [si/no]")

print(lista_palabras)