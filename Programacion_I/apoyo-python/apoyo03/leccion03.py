def sumar()->int:
    primer_numero = int(input("Ingrese un numero: "))
    segundo_numero= int(input("Ingrese otro numero: "))
    resultado = primer_numero + segundo_numero
    return resultado

def restar()->int:
    primer_numero = int(input("Ingrese un numero: "))
    segundo_numero= int(input("Ingrese otro numero: "))
    resultado = primer_numero - segundo_numero
    return resultado

resultado = sumar()
print(resultado)

# EVITANDO REPETICION DE CODIGO 

def pedir_datos():
    numero = int(input("Ingrese un numero"))
    return numero

def sumar()->int:
    primer_numero = pedir_datos()
    segundo_numero= pedir_datos()
    resultado = primer_numero + segundo_numero
    return resultado

# FUNCIONES GENERICAS

def pedir_datos(texto:str)->int:
    numero = input(texto)
    numero = int(numero)
    return numero

def sumar()->int:
    primero_numero = pedir_datos("Ingrese la primera cuenta")
    segundo_numero = pedir_datos("Ingrese la segunda cuenta")
    resultado = primero_numero + segundo_numero
    return resultado

################################################################

# pasaje por valor
def suma(numero):
    numero = numero + 1
    return numero

a = 3
b = suma(a)

print("Este es el valor de a: ", a)
print("Este es el valor de b: ", b)

# pasaje por referencia
def agregar_personas(lista, nombre):
    lista.append(nombre)

lista_nombres = ['Marina', 'Pedro']
print(lista_nombres)

agregar_personas(lista_nombres, "juan")
print(lista_nombres)

###################################################

def listar_por_caracteristicas(lista:list[dict], caracteristica:str)->None:
    for element in lista:
        print(element[caracteristica])

# listar_por_caracteristicas(...)

#################################################

# CADENA DE CARACTERES - es una lista de caracteres

# Es inmutable, las direcciones de memoria de cada caso son distintas
nombre = "Marina"
print(nombre)
print(id(nombre))

nombre = nombre + " cardozo"
print(nombre)
print(id(nombre))

# cantidad de caracteres
ejemplo = len(nombre)
print(ejemplo)

# convierte en maiuscula
print(nombre.upper())
# convierte en minuscula
print(nombre.lower())
# quita espacios en blanco de afuera
saludo = "    hola     "
print(saludo.strip())
# separa en listas lo que esta separado por espacios
prueba = nombre.split()
print(prueba)
#
prueba_dos = " - ".join(prueba)
print(prueba_dos)


#[inicio:fin:paso] - SLINCING

print(nombre[0]) # se imprime la primera letra

print(nombre[:6:2]) # va hasta indice 6 saltando de a dos 
