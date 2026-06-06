alumnos = []

while len(alumnos) < 4:
    nombre = input(f"Nombre del alumno {len(alumnos) + 1}: ").strip()
    
    if nombre != "":
        alumnos.append(nombre)
    else:
        print("El nombre no puede estar vacío.")

archivo = open("alumnos.txt", "w")
for alumno in alumnos:
    archivo.write(alumno + "\n")
archivo.close()

print("¡Archivo guardado!")
