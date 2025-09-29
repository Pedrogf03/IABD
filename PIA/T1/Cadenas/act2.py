# Realizar un programa que comprueba si una cadena leída por teclado comienza por una subcadena introducida por teclado. 

cadena = input("Introduzca una cadena: ")
subcadena = input("Introduzca la subcadena: ")

if cadena[:len(subcadena)] == subcadena:
  print("La cadena " + cadena + " comienza por la subcadena " + subcadena + ".")
else:
  print("La cadena '" + cadena + "' no comienza por la subcadena '" + subcadena + "'.")