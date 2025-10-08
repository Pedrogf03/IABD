# Diseñar el algoritmo correspondiente a un programa, que: 
  # Crea una tabla bidimensional de longitud 5x15 y nombre ‘marco’. 
  # Carga la tabla con dos únicos valores 0 y 1, donde el valor uno ocupará las  posiciones o elementos que delimitan la tabla, es decir, las más externas, mientras  que el resto de los elementos contendrán el valor 0.
  # Muestra el contenido de la tabla en pantalla.

tabla = []

for i in range(5):
  fila = []
  for j in range(15):
    if i == 0 or i == 4 or j == 0 or j == 14:
      fila.append(1)
    else:
      fila.append(0)
  tabla.append(fila)

print("Tabla marco:")
for fila in tabla:
  print("  ".join(str(num) for num in fila))