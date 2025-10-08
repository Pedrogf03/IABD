# Introducir una cadena de caracteres e indicar si es un palíndromo. Una palabra palíndroma es aquella que se lee igual adelante que atrás.

cadena = input("Introduzca una cadena: ")

if cadena == cadena[::-1]:
  print("La cadena es un palíndromo.")
else:
  print("La cadena no es un palíndromo.")