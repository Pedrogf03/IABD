# Crea un programa que pida un número al usuario un número de mes (por ejemplo, el 4) y  diga cuántos días tiene (por ejemplo, 30) y el nombre del mes. Debes usar listas. Para  simplificarlo vamos a suponer que febrero tiene 28 días.

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

num_mes = int(input("Introduce un número de mes (1-12): "))

if 1 <= num_mes <= 12:
  num_mes -= 1 
  if num_mes == 1:
    print(f"{meses[num_mes]} tiene 28 días.")
  elif num_mes % 2 == 0:
    print(f"{meses[num_mes]} tiene 31 días.")
  else:
    print(f"{meses[num_mes]} tiene 30 días.")
else:
  print("Número de mes inválido. Debe estar entre 1 y 12.")