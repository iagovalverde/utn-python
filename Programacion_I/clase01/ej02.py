'''
Debemos hacer un programa para que el usuario recuerde las reglas de estilo de
python, entonces debemos pedirle al usuario un número entre el 1 y el 8,
al ingresar el número debemos mostrarle que regla de estilo representa y su
descripción (Sacar la información de las diapositivas de las reglas de estilo).
En caso de que ingrese un numero fuera del rango deberá mostrarle al usuario
“Error, regla de estilo inexistente”

Nombre: Iago Valverde Pachiani
Div D
'''

numero_seleccionado = int(input("Ingrese la seleccion: [1-8]"))
while numero_seleccionado < 1 or numero_seleccionado > 8:
    numero_seleccionado = int(input("[ERROR] Regla de estilo inexistente. Ingrese la seleccion: [1-8]"))

match numero_seleccionado:
    case 1:
        print("¿Cuál es el sentido? \nSegún Guido van Rossum, el código es leído más veces que escrito, por lo que " 
            + "resulta importante escribir código que no sólo funcione, sino que además pueda ser leído con facilidad.")
    case 2: 
        print("¿Qué es PEP? \nPython Enhancement Proposal es un documento que proporciona información a la comunidad de " 
            + "Python, o que describe una nueva característica.")
    case 3: 
        print("¿Qué es PEP8? \nEs un conjunto de recomendaciones cuyo objetivo es ayudar a escribir código más legible y " 
            + "abarca desde cómo nombrar variables, al número máximo de caracteres que una línea debe tener.")
    case 4: 
        print("Indentado! \nPython no usa {} para designar bloques de código como otros lenguajes de programación, sino " 
            + "que usa bloques identados para indicar que un determinado bloque de código pertenece a por ejemplo un if.")
    case 5:
        print("Tamaño máximo linea! \nSe recomienda limitar el tamaño de cada línea a 79 caracteres, para evitar tener "
            + "que hacer scroll a la derecha.")
    case 6:
        print("Líneas en blanco! \nEl uso de espacios en blanco mejora la legibilidad del código, y es por lo que la PEP8 " 
            + "indica dónde debemos usar espacios y dónde no.")
    case 7: 
        print("Comentarios! \nCualquier comentario que contradiga el código es peor que ningún comentario." 
            + "\nSi actualizamos el código, se debe actualizar los comentarios para evitar crear inconsistencias. " 
            + "\nEvitar comentarios poco descriptivos que no aporten nada más allá de lo que ya se ve a simple vista.")
    case 8:
        print("Nombres! \nFunciones: Uso de snake_case, letras en minúscula separadas por guión bajo: mi_funcion." 
            + "\nVariables: Al igual que las funciones: variable, mi_variable."
            + "\nClases: Uso de CamelCase, usando mayúscula y sin barra baja: MiClase, ClaseDePrueba."
            + "\nMétodos: Al igual que las funciones, usar snake case: metodo, mi_metodo." 
            + "\nConstantes: Nombrarlas usando mayúsculas y separadas por guión bajas: UNA_CONSTANTE"
            + "\nMódulos: Igual que las funciones: modulo.py, mi_modulo.py.")















