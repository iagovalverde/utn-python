'''
La división de alimentos está trabajando en un pequeño software para cargar las
compras de ingredientes para la cocina de Industrias Wayne.
Realizar el algoritmo que permita ingresar los datos de una compra de ingredientes
para preparar comida al por mayor. En total, sabemos que se realizarán 15 compras
de ingredientes.
Se registra por cada compra:
1. PESO: (entre 10 y 100 kilos)
2. PRECIO POR KILO: (mayor a 0 [cero]).
3. TIPO VARIEDAD: (vegetal, animal, mezcla).
Además tener en cuenta que si compro más de 100 kilos en total tengo un 15% de
descuento sobre el precio bruto, o si compro más de 300 kilos en total, tengo un 25%
de descuento sobre el precio bruto.
Se desea saber:
A. El importe total a pagar, BRUTO sin descuento.
B. El importe total a pagar con descuento (Solo si corresponde).
C. Informar el tipo de alimento más caro.
D. El promedio de precio por kilo en total.

Nombre: Iago Valverde Pachiani
Div D
Ej 04
'''
acumulador_peso_total = 0
acumulador_precio_total = 0
bandera_alimento_mas_caro = 0
acumulador_precio_por_kilo = 0
contador_compras = 0

for i in range(15):
    peso_producto = float(input("Ingrese peso del producto en kg: [10-100] "))
    while peso_producto < 10 or peso_producto > 100:
        peso_producto = float(input("[ERROR] Reingrese peso del producto en kg: [10-100] "))
    precio_por_kilo = float(input("Ingrese precio por kg: "))
    while precio_por_kilo < 1:
        precio_por_kilo = float(input("[ERROR]Reingrese precio por kg: "))
    tipo_producto = input("Ingrese tipo: [vegetal / animal / mezcla] ")
    while tipo_producto != "vegetal" and tipo_producto != "animal" and tipo_producto != "mezcla":
        tipo_producto = input("[ERROR] Reingrese tipo: [vegetal / animal / mezcla] ")

    precio_por_compra = peso_producto * precio_por_kilo
    acumulador_peso_total += peso_producto
    acumulador_precio_total += precio_por_compra
    acumulador_precio_por_kilo += precio_por_kilo
    contador_compras += 1

    if bandera_alimento_mas_caro == 0 or precio_alimento_mas_caro < precio_por_kilo:
        precio_alimento_mas_caro = precio_por_kilo
        tipo_alimento_mas_caro = tipo_producto
        bandera_alimento_mas_caro = 1

if acumulador_peso_total > 300:
    descuento = 0.75
elif acumulador_peso_total > 100:
    descuento = 0.85
else:
    descuento = 1

importe_total = acumulador_precio_total * descuento 
valor_descuento = acumulador_precio_total - importe_total
promedio_precio_por_kilo_total = acumulador_precio_por_kilo / contador_compras

print(f"[AB] El importe total a pagar: {importe_total} \nCon descuento de: {valor_descuento}"
f"\n[C] El tipo de alimento más caro: {tipo_alimento_mas_caro}"
f"\n[D] Promedio de precio por kilo en total: {promedio_precio_por_kilo_total}")