mediciones = [
    ("temp", 18.5, "Aula 1"),
    ("humedad", 40, "Aula 1"),
    ("temp", 21.0, "Laboratorio"),
    ("presion", 1012, "Laboratorio"),
    ("humedad", 55, "Aula 2")
]

diccionario_aulas = {}
tipos = set()

for tipo, valor, lugar in mediciones:
    if lugar not in diccionario_aulas:
        diccionario_aulas[lugar] = []
    diccionario_aulas[lugar].append((tipo, valor))
    tipos.add(tipo)

print("Diccionario final:", diccionario_aulas)
print("Tipos encontrados:", tipos)