# Si tenemos una cadena con un nombre y apellidos, realizar un programa que muestre las iniciales en mayúsculas. 

cadena = input("Introduzca su nombre completo: ")

nombre = cadena.strip().split(" ")

iniciales = ""

for n in nombre:
  iniciales = iniciales + n[:1]
  
print(iniciales)