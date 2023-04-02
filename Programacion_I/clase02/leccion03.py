acumulador = 0
seguir = "si"

while seguir == "si":
    numero = int(input("Ingrese un numero: "))
    acumulador += numero

    seguir = input("Desea continuar? [si / no]")

print(f"Acumulado: {acumulador}")


# Do while 
acumulador = 0
seguir = True

while True:
    numero = int(input("Ingrese un numero: "))
    acumulador += numero

    seguir = input("Desea continuar? [si / no]")
    if seguir != "si":
        break

print(f"Acumulado: {acumulador}")