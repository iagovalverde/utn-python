## sin lista

respuesta = "si"

while respuesta == "si":
    marca_coche = input("Ingrese la marca: ")
    ano_coche = int(input("Ingrese el año: "))
    precio_coche = float(input("Ingrese precio: "))
    
    respuesta = input("Agregas más coches? [si / no]")

print(f"La marca es: {marca_coche} \nAno del coche: {ano_coche} \nPrecio: {precio_coche}")

