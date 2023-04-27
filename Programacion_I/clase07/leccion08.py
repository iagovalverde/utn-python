'''
def listar_agrupados(lista:list, clave):
    lista_colores = []
    for heroe in lista:
        color= heroe[clave]
        lista_colores.append(color)
    lista_colores_filtrada = set(lista_colores)
    
    for color in lista_colores_filtrada:
        print(color)
        for heroe in lista:
            if heroe[clave] == color:
                print(f"\t{heroe['nombre']}")
'''

## STRINGS
# son inmutables

# metodo strip -> quita los espacios
mi_cadena = "      hola mundo     "
mi_cadena = mi_cadena.strip()
print(mi_cadena)

# metodo upper -> convierte la cadena a maiusculas
mi_cadena = mi_cadena.upper()
print(mi_cadena)

# metodo lower -> convierte la cadena a minusculas
mi_cadena = mi_cadena.lower()
print(mi_cadena)

# metodo capitalize -> convierte la primera letra de la cadena en maiuscula
mi_cadena = mi_cadena.capitalize()
print(mi_cadena)

# metodo replace -> cambia parte de la cadena en lo que declaras despues de la coma
mi_cadena = mi_cadena.replace("mundo", "zzz")
print(mi_cadena)

# metodo split
mi_cadena = "Python, Java, JavaScript, C#"
lista_split = mi_cadena.split(",")#"," -> caracter delimitador
print(lista_split)
for lenguaje in lista_split:
    print(lenguaje.strip())

# metodo join
separador = "/"
dia = "10"
mes = "9"
año = "2005"
fecha = separador.join([dia, mes, año])
print(fecha)

# zfill llena con 0s a la izquierda
cadena = "123"
cadena = cadena.zfill(5)
print(cadena)

# isalpha devuelve True si es alfabetica
mi_cadena = "holamundo"
print(mi_cadena.isalpha())

# isalnum devuelve True si es alfanumerica
mi_cadena = "hola3"
print(mi_cadena.isalnum())

# len
cadena = "hola mundo"
print(len(cadena))

# count averigua cuantas veces encuentra la palabra 'la'
mi_cadena = "holalala"
print(mi_cadena.count("la"))

# hacer un print de parte de la cadena
cadena = "hola mundo"
print(cadena[5:10])
