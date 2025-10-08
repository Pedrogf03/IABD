# Diseñar el algoritmo correspondiente a un programa, que: 
  # Crea una tabla (lista con dos dimensiones) de 5x5 enteros. 
  # Carga la tabla con valores numéricos enteros. 
  # Suma todos los elementos de cada fila y todos los elementos de cada columna visualizando los resultados en pantalla. 

import random

tabla = []

for i in range(5):
  fila = []
  for j in range(5):
    fila.append(random.randint(1, 100))
  tabla.append(fila)

suma_filas = [sum(fila) for fila in tabla]
suma_columnas = [sum(tabla[i][j] for i in range(5)) for j in range(5)]

print("Tabla:")
for idx, fila in enumerate(tabla):
    # Convertimos cada número a string y lo alineamos a la derecha con 4 espacios
    fila_str = " ".join(str(num).rjust(4) for num in fila)
    print(f"{fila_str} | {suma_filas[idx]:>4}")

print("-" * 32)

# Imprimir suma de columnas alineada con la tabla
columnas_str = " ".join(str(num).rjust(4) for num in suma_columnas)
print(f"{columnas_str} | {sum(suma_filas) + sum(suma_columnas)}")

