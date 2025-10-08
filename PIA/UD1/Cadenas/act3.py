# Pide una cadena y un carácter por teclado (valida que sea un carácter) y muestra cuantas veces aparece el carácter en la cadena. 

cadena = input("Introduzca una cadena: ")
caracter = input("Introduzca el caracter que busca: ")

while len(caracter) != 1:
  print("Error. Debe introducir un solo caracter.")
  caracter = input("Introduzca el caracter que busca: ")

print("El caracter '" + caracter + "' aparece " + str(cadena.count(caracter)) + " veces en la cadena '" + cadena + "'.")