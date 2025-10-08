# Realizar un programa que compruebe si una cadena contiene una subcadena. Las dos cadenas se introducen por teclado. 

cadena = input("Introduzca una cadena: ")
subcadena = input("Introduzca la subcadena: ")

if subcadena in cadena:
    print("La cadena contiene la subcadena.")
else:
    print("La cadena NO contiene la subcadena.")