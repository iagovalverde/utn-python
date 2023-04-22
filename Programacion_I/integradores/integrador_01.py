'''
Desafio Integrador 01
Nombre: Iago Valverde Pachiani
Div - 1D
'''

from data_stark import lista_personajes 
from funciones_01 import *
from os import system

menu_principal = ["1. Mostrar el nombre de cada héroe",
                "2. Mostrar héroes con sus alturas",
                "3. Mostrar nombre del héroe más alto",
                "4. Mostrar nombre del héroe más bajo",
                "5. Mostrar altura promedio de los héroes",
                "6. Mostrar héroe más y menos pesado",
                "7. Mostrar cuantos héroes con cada color de ojos",
                "8. Mostrar cuantos héroes con cada color de pelo",
                "9. Mostrar cuantos héroes con cada tipo de inteligencia",
                "10. Listar los héroes por color de ojos",
                "11. Listar los héroes por color de pelo",
                "12. Listar los héroes por tipo de inteligencia",
                "13. Salir"
]

sub_menu = ["Sub-menu",
            "1. Mostrar entre todos héroes",
            "2. Mostrar entre héroes masculinos",
            "3. Mostrar entre héroes femeninos",
            "4. Salir"
]

def mostrar_menu():
    for opcion in menu_principal:
        print(opcion)

def mostrar_sub_menu():
    for opcion in sub_menu:
        print(opcion)

while True:
    mostrar_menu()
    respuesta = int(input("Ingrese una opcion: "))
    match respuesta:
        case 1:
            while True:
                mostrar_sub_menu()
                respuesta = int(input("Ingrese una opcion "))
                match respuesta:
                    case 1:
                        genero = None
                        mostrar_nombre_heroes(lista_personajes, genero)
                    case 2:
                        genero = 'M'
                        mostrar_nombre_heroes(lista_personajes, genero)
                    case 3:
                        genero = 'F'
                        mostrar_nombre_heroes(lista_personajes, genero)
                    case 4:
                        break
        case 2:
            mostrar_nombre_altura_heroes(lista_personajes)
        case 3:
            while True:
                mostrar_sub_menu()
                respuesta = int(input("Ingrese una opcion "))
                match respuesta:
                    case 1:
                        pass
                    case 2:
                        genero = 'M'
                        mostrar_heroe_mas_alto(lista_personajes, genero)
                    case 3:
                        genero = 'F'
                        mostrar_heroe_mas_alto(lista_personajes, genero)
                    case 4:
                        break
        case 4:
            while True:
                mostrar_sub_menu()
                respuesta = int(input("Ingrese una opcion "))
                match respuesta:
                    case 1:
                        pass
                    case 2:
                        genero = 'M'
                        mostrar_heroe_mas_bajo(lista_personajes, genero)
                    case 3:
                        genero = 'F'
                        mostrar_heroe_mas_bajo(lista_personajes, genero)
                    case 4:
                        break
        case 5:
            while True:
                mostrar_sub_menu()
                respuesta = int(input("Ingrese una opcion "))
                match respuesta:
                    case 1:
                        genero = None
                        calcular_promedio_altura(lista_personajes, genero)
                    case 2:
                        genero = 'M'
                        calcular_promedio_altura(lista_personajes, genero)
                    case 3:
                        genero = 'F'
                        calcular_promedio_altura(lista_personajes, genero)
                    case 4:
                        break
        case 6:
            calcular_peso_max(lista_personajes)
            calcular_peso_min(lista_personajes)
        case 7:
            tipo = 'color_ojos'
            calcular_tipo_caracteristica(lista_personajes, tipo)
        case 8:
            tipo = 'color_pelo'
            calcular_tipo_caracteristica(lista_personajes, tipo)
        case 9:
            tipo = 'inteligencia'
            calcular_tipo_caracteristica(lista_personajes, tipo)
        case 10:
            tipo = 'color_ojos'
            listar_heroes_caracteristica(lista_personajes, tipo)
        case 11:
            tipo = 'color_pelo'
            listar_heroes_caracteristica(lista_personajes, tipo)
        case 12:
            tipo = 'inteligencia'
            listar_heroes_caracteristica(lista_personajes, tipo)
        case 13:
            break
