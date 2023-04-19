'''
Una concesionaria de autos nos pide desarrollar un sistema para controlar el stock de
autos que tienen disponible a la venta. Para esto se necesita saber de cada auto: la
marca, el año del modelo y el precio (validar los tipos de datos ingresados) y
mostrarlos por pantalla en forma secuencial y ordenada. Realizar el ejercicio sin usar
listas primero, y despues usando listas y comparar la composición del código.
'''

## sin lista

respuesta = "si"

while respuesta == "si":
    marca_coche = input("Ingrese la marca: ")
    ano_coche = int(input("Ingrese el año: "))
    precio_coche = float(input("Ingrese precio: "))
    
    respuesta = input("Agregas más coches? [si / no]")

print(f"La marca es: {marca_coche} \nAno del coche: {ano_coche} \nPrecio: {precio_coche}")

