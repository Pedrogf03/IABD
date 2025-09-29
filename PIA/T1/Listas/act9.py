# Queremos guardar la temperatura mínima y máxima de 5 días. Realiza un programa que  de la siguiente información:
  # La temperatura media de cada día 
  # Los días con menos temperatura 
  # Se lee una temperatura por teclado y se muestran los días cuya temperatura máxima coincide con ella. si no existe ningún día se muestra un mensaje de información.
  
print("Introduce las temperaturas mínimas y máximas de 5 días.")

dias = [[], [], []]  # Lista de tuplas (temp_min, temp_max, temp_media)

for i in range(5):
  temp_min = float(input(f"Temperatura mínima del día {i+1}: "))
  dias[0].append(temp_min)
  temp_max = float(input(f"Temperatura máxima del día {i+1}: "))
  dias[1].append(temp_max)
  temp_media = (temp_min + temp_max) / 2
  dias[2].append(temp_media)
  print("--------------------")

print("Temperaturas medias de cada día:")
for i in range(5):
  print(f"Día {i+1}: {dias[2][i]:.0f}°C")

temp_minima = min(dias[0])
dias_menor_temp = [i+1 for i in range(5) if dias[0][i] == temp_minima]
print(f"Los días {dias_menor_temp} tienen la temperatura mínima: {temp_minima:.0f}°C")

temp_buscada = float(input("Introduce una temperatura máxima a buscar: "))
dias_con_temp = [i+1 for i in range(5) if dias[1][i] == temp_buscada]
if dias_con_temp:
  print(f"Los días con temperatura máxima de {temp_buscada:.0f}°C son los días {dias_con_temp}")
else:
  print(f"No hay días con temperatura máxima de {temp_buscada:.0f}°C.")

