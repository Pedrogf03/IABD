# Escribe un programa que pida un número al usuario e imprima si el número está en uno de los siguientes rangos:
  # Menor que 0.
  # Entre 0 y 10.
  # Mayor que 10.

num = float(input("Introduce un número: "))

if num < 0:
  print("El número es menor que 0.")
elif num <= 10:
  print("El número está entre 0 y 10.")
else:
  print("El número es mayor que 10.")