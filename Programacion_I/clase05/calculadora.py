# FUNCIONES #

def sumar_numeros(primer_numero:int, segundo_numero:int)-> None: 
    suma = primer_numero + segundo_numero
    return suma

def restar_numeros(primer_numero:int, segundo_numero:int)-> int: 
    resta = primer_numero - segundo_numero
    return resta

def multiplicar_numeros(primer_numero: int, segundo_numero: int)->None:
    multiplicacion = primer_numero * segundo_numero
    return multiplicacion

def dividir_numeros(primer_numero:int, segundo_numero:int): 
    division = None
    if segundo_numero != 0:
        division = primer_numero / segundo_numero
    return division

bandera_ingreso = False
while True:
    opcion = int(input("1. Ingresar numeros \n2. Restar \n3. Multiplicar \n4. Dividir \n5. Sumar \n6. Salir \n Ingrese una opcion: "))
    match opcion:
        case 1:
            x = int(input("Ingrese un numero: "))
            y = int(input("Ingrese otro numero: "))
            bandera_ingreso = True
        case 2:
            if bandera_ingreso == True:
                resultado = restar_numeros(x,y)
                print(f"El resultado de la resta es: {resultado}")
            else: 
                print("No hay operandos ingresados")
        case 3:
            if bandera_ingreso == True:
                resultado = multiplicar_numeros(x,y)
                print(f"El resultado de la multiplicacion es: {resultado}")
            else: 
                print("No hay operandos ingresados")
        case 4:
            if bandera_ingreso == True:
                resultado = dividir_numeros(x,y)
                if(resultado != None):
                    print(f"El resultado de la division es: {resultado}")
                else:
                    print("[ERROR] No se puede dividir por cero")
            else:
                print("No hay operandos ingresados")
        case 5:
            if bandera_ingreso == True:
                resultado = sumar_numeros(x,y)
                print(f"El resultado de la suma es: {resultado}")
            else: 
                print("No hay operandos ingresados")
        case 6:
            break