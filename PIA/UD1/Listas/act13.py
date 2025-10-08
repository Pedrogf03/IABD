# De una empresa de transporte se quiere guardar el nombre de los conductores que tiene,  y los kilómetros que conducen cada día de la semana.
# Para guardar esta información se van a utilizar dos arrays: 
  # nombres: Lista para guardar los nombres de los conductores. 
  # kms: Tabla para guardar los kilómetros que realizan cada día de la semana. 
# Se quiere generar una nueva lista (“total_kms”) con los kilómetros totales que realza cada  conductor.
# Al finalizar se muestra la lista con los nombres de conductores y los kilómetros que ha realizado.

nombres = []
kms = []
total_kms = []

while True:
  nombre = input("Introduce el nombre del conductor (o 'fin' para terminar): ")
  if nombre.lower() == 'fin':
    break
  nombres.append(nombre)
    
  km_dia = []
  for dia in ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]:
    km = float(input(f"Introduce los kilómetros recorridos el {dia}: "))
    km_dia.append(km)
  kms.append(km_dia)

for i in range(len(nombres)):
  total = sum(kms[i])
  total_kms.append(total)

dias = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]

# Definir ancho de columna para centrar
ancho = 6

# Imprimir encabezado (nombres)
print("       ", end="")  # espacio para la columna de días
print("".join(nombre.center(ancho) for nombre in nombres))

# Imprimir cada fila con el día y los kms
for dia_idx in range(7):
    print(dias[dia_idx].ljust(5), end=" ")  # día alineado a la izquierda
    print("".join(str(int(kms[i][dia_idx])).center(ancho) for i in range(len(nombres))))

