# Escribe un programa que pida al usuario un número e imprima si es positivo o negativo.

num = float(input("Introduce un número: "))

if num > 0:
  print("El número es positivo.")
elif num < 0:
  print("El número es negativo.")
else:
  print("El número es cero.")