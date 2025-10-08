# Realizar un programa que lea una cadena por teclado y convierta las mayúsculas a minúsculas y viceversa. 

cadena = input("Introduzca una cadena: ")

cadena2 = ""

for c in cadena:
  if c.isupper():
    cadena2 = cadena2 + c.lower()
  elif c.islower():
    cadena2 = cadena2 + c.upper()

print(cadena2)