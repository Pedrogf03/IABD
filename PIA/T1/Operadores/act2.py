# Escribe un programa que pida al usuario dos números y muestre cuál de ellos es mayor o si son iguales.

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

if num1 > num2:
  print("El primer número es mayor.")
elif num1 < num2:
  print("El segundo número es mayor.")
else:
  print("Los dos números son iguales.")