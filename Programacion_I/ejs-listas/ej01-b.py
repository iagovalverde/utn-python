lista_autos = []
respuesta = "si"

while respuesta == "si":
    marca_auto = input("Ingrese la marca: ")
    fecha_auto = int(input("Ingrese el anõ: "))
    precio_auto = float(input("Ingrese el precio: "))
    while precio_auto < 1:
        precio_auto = float(input("[ERROR] Reingrese precio: "))
    
    datos_auto = {"marca": marca_auto, "fecha": fecha_auto, "precio": precio_auto}
    lista_autos.append(datos_auto)
    respuesta = input("Ingresas mas autos? [si/no]")

for auto in lista_autos:
    print(f"Marca: {auto['marca']} - Anõ: {auto['fecha']} - Precio: {auto['precio']}")
