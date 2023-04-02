color = "azul"

if color == "azul":
    print("Es azul")
else: 
    if color == "verde":
        print("Es verde")
    else:
        if color == "amarillo":
            print("Es amarillo")
        else:
            if color == "rojo":
                print("Es rojo")
            else:
                print("Es otro color")


if color == "azul":
    print("Es azul")
elif color == "verde":
    print("Es verde")
elif color == "amarillo":
    print("Es amarillo")
elif color == "rojo":
    print("Es rojo")
else:
    print("Es otro color")


color = "azul"
match color:
    case "azul":
        print("azul")
    case "rojo":
        print("rojo")
    case other: # case _
        print("Es otro color")