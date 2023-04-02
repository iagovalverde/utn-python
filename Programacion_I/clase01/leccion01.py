# comentario una linea
'''
comentario varias lineas
'''
# limpiar pantalla - system("cls")

# nombre_paciente (snakecase)

# bandera_maximo = True


nombre = "Jose"
edad = 25

if (nombre == "Juan" and
    edad > 20):
    print("Gracias por utilizar nuestro sistema")
else:
    if nombre == "Maria":
        print("Bienvenida Maria")
    else:
        if nombre == "Jose":
            print("Bienvenido Jose")
        else:
            print("Usted no se llama Juan, ni Maria, ni Jose")

if 3>5:
    pass

'''
CASTING

numero = input("Ingrese un numero: ")

int()
float()
str()
'''
numero = 55
cadena = "texto"

print(f"La cadena es: {cadena}\nEl numero es: {numero:.2f}")

#print("La cadena es: {0}".format(cadena))
#print("El numero es: {0}".format(numero))

#print("La cadena es: " + cadena)
#print("El numero es: " , numero)
