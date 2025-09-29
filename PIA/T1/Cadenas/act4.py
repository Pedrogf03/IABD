# Suponiendo que hemos introducido una cadena por teclado que representa una frase (palabras separadas por espacios), realiza un programa que cuente cuántas palabras tiene.

cadena = input("Introduzca una cadena: ")

numPalabras = cadena.strip().split(" ")

print("La cadena contiene " + str(len(numPalabras)) + " palabras.")