import re

'''
\t = tabulacion
\n salto de linea
'''


### SPLIT ###
print("-----------SPLIT-----------")

print(re.split(" ", "hola mundo, 1c"))
print(re.split("[a-z ]+", "hola mundo, 125c"))
print(re.split("[0-9 ]+", "hola mundo, 125c"))
print(re.split("[a-z]|[0-9| ]", "hola mundo @@ 1253 chau"))


### SEARCH ###
print("-----------SEARCH-----------")
'''
group(): devuelve la cadena que coincide con el patrón
start(): devuelve la posición de inicio de la coincidencia en la cadena original
end(): devuelve la posición final de la coincidencia en la cadena original
span(): devuelve una tupla que contiene la posición de inicio y final de la coincidencia en la cadena original
'''
# devuelve None si no encuentra lo que se busca dentro de la cadena
print(re.search(" ", "hola"))

# devuelve Match con una tupla diciendo en que indices encuentra lo que se busca
print(re.search("como", "hola como estan?"))
print(re.search("como", "hola como estan?").span())
print(re.search("como", "hola como estan?").start())
print(re.search("como", "hola como estan?").end())

print(re.search("[0-9]", "texto con numeros: 123 y letras: aaa"))
print(re.search("[0-9]+", "texto con numeros: 123 y letras: aaa"))

### FINDALL ###
print("------------FINDALL-----------")
#{3,6} como minimo 3 como maximo 6

texto = "Un 1 Dos 2 tres 3 cuatro"
print(re.findall(" ", texto))
print(re.findall("[0-9]+", texto))
print(re.findall("[a-zA-Z]+", texto))
print(re.findall("[a-zA-Z]{3,6}", texto))

### SUB ###
print("------------SUB-----------")

# patron que busco, por lo que voy a reemplazar, de donde
texto = "abc abc ccc ddd     abc aaa"
result = re.sub("abc", "xyz", texto)
print(result)

# donde encuentre más de un espacio juntos, cambiar por apenas un espacio -> \s = 1 espacio
result = re.sub(r'\s+', " ", texto)
print(texto)
print(result)
# donde encuentre grupos de 2 espacios, cambiar por 1 espacio
result = re.sub(r'\s\s', " ", texto)

