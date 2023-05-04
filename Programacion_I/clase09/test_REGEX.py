import re

##### BIZARRAP 

texto = "QUEVEDO || BZRP Music Sessions #52"

print(re.split(" \|{2} ", texto))
print(re.split("[\|#]+", texto))

print("---------FECHA----------")

fecha = "2022-02-03 19:20:33"

# fecha
print(re.findall("[0-9]{4}-[0-9]{2}-[0-9]{2}", fecha))
# año
print(re.findall("[0-9]{4}", fecha))
# mes
# excluir los guiones
print(re.findall("-([0-9]{2})-", fecha))
# dia
print(re.findall("-([0-9]{2}) ", fecha))
# separar la fecha
print(re.split("-| ", fecha))

# HACER LO MISMO 
# numero del 0 al 9 como {minimo x, maximo y}
año = "([0-9]{2,4})"
mes = "([0-9]{1,2})"
dia = "([0-9]{1,2})" 

print(re.findall(f"{año}-{mes}-{dia}", fecha))
