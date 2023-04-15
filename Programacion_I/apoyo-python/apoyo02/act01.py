animes_90s = [
    {"nombre": "Dragon Ball Z", "año": 1989, "temporadas": 9, "personaje_principal": "Goku"},
    {"nombre": "Sailor Moon", "año": 1992, "temporadas": 5, "personaje_principal": "Usagi Tsukino"},
    {"nombre": "Pokemon", "año": 1997, "temporadas": 23, "personaje_principal": "Ash Ketchum"},
    {"nombre": "Digimon Adventure", "año": 1999, "temporadas": 1, "personaje_principal": "Tai Kamiya"},
    {"nombre": "Evangelion", "año": 1995, "temporadas": 1, "personaje_principal": "Shinji Ikari"}
]

# # Hacer una cantidad de vueltas de forma determinada
# for i in range(10):
#     print(i)

# # Recorrer la lista contando la cantidad de elementos que tiene esa lista
# range(len(animes_90s))

temporadas = []

# Obtener informacion de los elementos que se encuentran en la lista
for anime in animes_90s:
    if anime['temporadas'] > 1:
        temporadas.append(anime['nombre'])

print(temporadas)

