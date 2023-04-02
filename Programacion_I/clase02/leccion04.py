#mi_lista = list(range(10,20,2))
#print(mi_lista)

acumulador = 0
for x in range(5):
    numero = int(input("Ingrese un numero: "))
    acumulador += numero
print(f"Acumulado: {acumulador}")


lista_nombres = ["Luis", "Nicolas", "Federico", "Micaela", "Silvina"]
for nombre in lista_nombres:
    if nombre == "Federico": # salta e ignora el nombre Federico
        continue
    print(nombre)

## att Python
# conda create -n python 3 python=3.10 anaconda