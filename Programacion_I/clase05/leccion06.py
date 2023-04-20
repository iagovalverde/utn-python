# FUNCIONES #

# NO TIENE PARAMETROS NI RETORNO (PEORES)
def sumar_numeros()-> None: # Implementacion de la funcion
    primer_numero = int(input("Ingrese el primer numero: "))
    segundo_numero = int(input("Ingrese el segundo numero: "))

    suma = primer_numero + segundo_numero
    print(f"La suma es: {suma}")


# TIENE RETORNO PERO NO TIENE PARAMETROS
def restar_numeros()-> int: # Implementacion de la funcion
    primer_numero = int(input("Ingrese el primer numero: "))
    segundo_numero = int(input("Ingrese el segundo numero: "))

    resta = primer_numero - segundo_numero

    return resta


# NO TIENE RETORNO PERO SI TIENE PARAMETROS
def multiplicar_numeros(primer_numero: int, segundo_numero: int)->None:
    # los numeros vienen por parametros (formales)
    multiplicacion = primer_numero * segundo_numero
    print(f"El resultado de la multiplicacion es: {multiplicacion}")


# TIENE PARAMETROS Y RETORNO (MEJORES)
def dividir_numeros(primer_numero:int, segundo_numero:int)->float: 
    division = None
    if segundo_numero != 0:
        division = primer_numero / segundo_numero
    return division

print("Hola, bienvenido a mi programa!")
sumar_numeros() # LLamada a la funcion
print("Gracias por sumar...")

resultado_resta = restar_numeros()
print(f"El resultado de la resta es: {resultado_resta}")

multiplicar_numeros(5,9) # Parametros actuales
x = int(input("Ingrse un numero: "))
y = int(input("Ingrese otro numero: "))

multiplicar_numeros(x,y)

resultado_division = dividir_numeros(6,2)
print(f"El resultado de la division: {resultado_division}")

resultado_division = dividir_numeros(x,y)
print(f"El resultado de la division: {resultado_division}")