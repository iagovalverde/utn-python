# LISTAS # 
# # se accede a sus elementos por su indice

# mi_lista = []
# print(type(mi_lista))

# mi_lista_segunda = list()
# print(type(mi_lista_segunda))

mi_lista = [1,2,"marina",['a','b','c'], True]
#           0 1    2           3          4
#          -5-4   -3          -2         -1

print(mi_lista[3])

if type(mi_lista[3]) == list:
    sub_lista = mi_lista[3][1]
    print(sub_lista)
else:
    print("te equivocaste")

mi_lista.append("hola")

# inicio:final:paso    SLICING
print(mi_lista[1:3])
print(mi_lista[::2]) # recorrer de a dos

print(mi_lista)

# ------------------------------------------

mi_nueva_lista = [[1,2,3], [3,4], [5,6,7]]

# LISTA PARALELA #

notas_1 = [7,8,9]
notas_2 = [10,8,9]
alumnos = ['pepe', 'juan', 'emma']

for i in range(3):
    print(f"Alumno: {alumnos[i]} - Primera Nota: {notas_1[i]} - Segunda Nota: {notas_2[i]}")

# DICCIONARIOS # 
# se accede a sus elementos por su clave

mi_diccionario = {1: "marina", "apellido": ["cardozo", "pagura"]}
print(mi_diccionario['apellido'])

# agregar un elemento al diccionario
mi_diccionario["edad"] = 27
print(mi_diccionario)

mi_diccionario["edad"] = 15
print(mi_diccionario)

# borrar un elemento
del mi_diccionario["edad"]
print(mi_diccionario)


# TUPLAS #
# es inmutable

mi_tupla = (1, '2', True)
print(mi_tupla)

# SET # 
# desordena y no se repiten elementos

mi_set = set([1,2,2,3,4,4,5])
print(mi_set)
print(type(mi_set))

