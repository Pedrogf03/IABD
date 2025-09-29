# Pide una cadena y dos caracteres por teclado (valida que sea un carácter), sustituye la aparición del primer carácter en la cadena por el segundo carácter. 

cadena = input("Introduzca una cadena: ")

char1 = input("Introduzca el primer caracter: ")
char2 = input("Introduzca el segundo caracter: ")

if len(char1) == 1 and len(char2) == 1:
  cadena = cadena.replace(char1, char2)
  print(cadena)
else:
  print("Introduzca un caracter válido.")