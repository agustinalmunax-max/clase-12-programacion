diccionario_ciudades = {}

with open("temperaturas.txt", "r") as archivo:
    for linea in archivo:
        if linea.strip():
            ciudad, temperatura = linea.strip().split(";")

        if ciudad not in diccionario_ciudades:
            diccionario_ciudades[ciudad] = []
        diccionario_ciudades[ciudad].append(temperatura)

print("Resultado de la lectura:", diccionario_ciudades)