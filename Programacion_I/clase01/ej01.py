'''
La división de higiene está trabajando en un control de stock para productos
sanitarios. Debemos realizar la carga de
una compra de productos de prevención de contagio, de cada una debe obtener los
siguientes datos:
· El tipo (&quot;barbijo&quot;, &quot;jabón&quot; o &quot;alcohol&quot;)
· El precio
· La cantidad de unidades
· La marca
· El fabricante

Nombre: Iago Valverde Pachiani
Div D
Ej 01
'''

tipo_producto = input("Ingrese tipo de producto: [barbijo / jabon / alcohol]")
precio_producto = float(input("Ingrese precio: "))
cantidad_unidades = int(input("Ingrese cantidad de unidades: "))
marca_producto = input("Ingrese la marca: ")
fabricante_producto = input("Ingrese el fabricante: ")

print(f"El tipo producto es: {tipo_producto}"
f"\nEl precio es: {precio_producto}"
f"\nLa cantidad de unidades: {cantidad_unidades}"
f"\nLa marca: {marca_producto}"
f"\nFabricante: {fabricante_producto}")
