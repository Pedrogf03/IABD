# Queremos guardar los nombres y la edades de los alumnos de un curso.
# Realiza un programa que introduzca el nombre y la edad de cada alumno.
# El proceso de lectura de datos terminará cuando se introduzca como nombre un asterisco (*).
# Al finalizar se mostrará los siguientes datos: 
  # Todos lo alumnos mayores de edad. 
  # Los alumnos mayores (los que tienen más edad).

print("Introduce los nombres y edades de los alumnos. Para terminar, introduce '*' como nombre.")

alumnos = [[], []]  # Lista de tuplas (nombre, edad)

while True:
  nombre = input("Nombre del alumno: ")
  if nombre == '*':
    break
  alumnos [0].append(nombre)
  edad = int(input(f"Edad de {nombre}: "))
  alumnos[1].append(edad)

mayores_edad = [alumnos[0][i] for i in range(len(alumnos[0])) if alumnos[1][i] >= 18]

print("\nAlumnos mayores de edad:")

for alumno in mayores_edad:
  print(alumno)

edad_maxima = max(alumnos[1]) if alumnos[1] else None
alumnos_mayores = [alumnos[0][i] for i in range(len(alumnos[0])) if alumnos[1][i] == edad_maxima] if edad_maxima is not None else []

print("\nAlumnos con mayor edad:")

for alumno in alumnos_mayores:
  print(alumno) 
