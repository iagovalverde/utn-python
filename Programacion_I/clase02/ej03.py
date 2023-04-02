'''
Es la gala final de Gran Hermano y la producción nos pide un programa para contar
los votos de los televidentes y saber cuál será el participante que ganará el juego.
Los participantes finalistas son: Nacho, Julieta y Marcos.
El televidente debe ingresar:
● Nombre del votante
● Edad del votante (debe ser mayor a 13)
● Género del votante (masculino, femenino, otro)
● El nombre del participante a quien le dará el voto positivo.
No se sabe cuántos votos entrarán durante la gala.
Se debe informar al usuario:
A. El promedio de edad de las votantes de género femenino
B. Cantidad de personas de género masculino entre 25 y 40 años que votaron a
Nacho o Julieta.
C. Nombre del votante más joven que votó a Nacho.
D. Nombre de cada participante y porcentaje de los votos qué recibió.
E. El nombre del participante que ganó el reality (El que tiene más votos)

Nombre: Iago Valverde Pachiani
Div D
Ej 03
'''

respuesta = "si"
contador_votantes_femenino = 0
acumulador_votantes_femenino = 0
promedio_edad_votantes_femenino = 0
contador_votos_masculino_nacho_julieta = 0
bandera_mas_joven = 0
edad_votante_mas_joven_nacho = 0
contador_votos_recibidos_nacho = 0
contador_votos_recibidos_julieta = 0
contador_votos_recibidos_marcos = 0
contador_total_votos = 0

while respuesta == "si":
    nombre_votante = input("Ingrese su nombre: ")
    edad_votante = int(input("Ingrese su edad: [mayor a 13]"))
    while edad_votante < 13:
        edad_votante = int(input("[ERROR] Reingrese edad mayor a 13: "))
    genero_votante = input("Ingrese genero: [masculino / femenino / otro]")
    while genero_votante != "masculino" and genero_votante != "femenino" and genero_votante != "otro":
        genero_votante = input("[ERROR] Reingrese genero: [masculino / femenino / otro]")
    nombre_participante = input("Ingrese el nombre del participante que recibe tu voto: [Nacho / Julieta / Marcos]")
    while nombre_participante != "Nacho" and nombre_participante != "Julieta" and nombre_participante != "Marcos":
        nombre_participante = input("[ERROR] Reingrese su voto: [Nacho / Julieta / Marcos]")

    contador_total_votos += 1

    match genero_votante:
        case "femenino":
            contador_votantes_femenino += 1
            acumulador_votantes_femenino += edad_votante
        case "masculino":
            if edad_votante > 25 and edad_votante < 40:
                if nombre_participante == "Nacho" or nombre_participante == "Julieta":
                    contador_votos_masculino_nacho_julieta += 1
        case "otro":
            pass

    match nombre_participante:
        case "Nacho":
            if bandera_mas_joven == 0 or edad_votante_mas_joven_nacho > edad_votante:
                edad_votante_mas_joven_nacho = edad_votante
                nombre_votante_mas_joven_nacho = nombre_votante
                bandera_mas_joven = 1
            contador_votos_recibidos_nacho += 1
        case "Julieta":
            contador_votos_recibidos_julieta += 1
        case "Marcos":
            contador_votos_recibidos_marcos += 1

    respuesta = input("Hay más votantes? [si / no]")

if contador_votantes_femenino > 0:
    promedio_edad_votantes_femenino = acumulador_votantes_femenino / contador_votantes_femenino

porcentaje_votos_nacho = contador_votos_recibidos_nacho / contador_total_votos * 100
porcentaje_votos_julieta = contador_votos_recibidos_julieta / contador_total_votos * 100
porcentaje_votos_marcos = contador_votos_recibidos_marcos / contador_total_votos * 100

if contador_votos_recibidos_nacho > contador_votos_recibidos_julieta and contador_votos_recibidos_nacho > contador_votos_recibidos_marcos:
    ganador_reality = "Nacho"
elif contador_votos_recibidos_julieta > contador_votos_recibidos_marcos and contador_votos_recibidos_julieta >= contador_votos_recibidos_nacho:
    ganador_reality = "Julieta"
elif contador_votos_recibidos_marcos > contador_votos_recibidos_julieta and contador_votos_recibidos_marcos > contador_votos_recibidos_nacho:
    ganador_reality = "Marcos"

print(f"[A] Promedio edad votantes femenino: {promedio_edad_votantes_femenino}"
f"\n[B] Cantidad personas genero masculino, edad entre 25 y 40 votantes de Nacho o Julieta: {contador_votos_masculino_nacho_julieta}"
f"\n[C] Votante más joven que votó a Nacho: {nombre_votante_mas_joven_nacho}"
f"\n[D] Nacho recibio en porcentaje: {porcentaje_votos_nacho} \nJulieta recibio en porcentaje: {porcentaje_votos_julieta} \nMarcos recibio en porcentaje: {porcentaje_votos_marcos}"
f"\nEl ganador del reality: {ganador_reality}")