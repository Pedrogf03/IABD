# Realizar un programa que dada una cadena de caracteres por caracteres, genere otra cadena resultado de invertir la primera.

cadena = input("Introduzca una cadena: ")

invertida = ""

for c in cadena:
  invertida = c + invertida

print(invertida)