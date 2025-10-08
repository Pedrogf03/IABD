# Diseñar el algoritmo correspondiente a un programa, que: 
  # Crea una tabla bidimensional de longitud 5x5 y nombre ‘diagonal’. 
  # Carga la tabla de forma que los componentes pertenecientes a la diagonal de la matriz tomen el valor 1 y el resto el valor 0. 
  # Muestra el contenido de la tabla en pantalla.

diagonal = []

for i in range(5):
  fila = []
  for j in range(5):
    if i == j:
      fila.append(1)
    else:
      fila.append(0)
  diagonal.append(fila)

print("Tabla diagonal:")
for fila in diagonal:
  print("  ".join(str(num) for num in fila))
  