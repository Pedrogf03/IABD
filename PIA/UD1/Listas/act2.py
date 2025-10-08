# Crea una lista e inicializala con 5 cadenas de caracteres leídas por teclado. Copia los elementos de la lista en otra lista pero en orden inverso, y muestra sus elementos por la pantalla. 

lista = []

for i in range(5):
  cadena = input("Introduce una cadena de caracteres: ")
  lista.append(cadena)

lista_invertida = lista[::-1]

for cadena in lista_invertida:
  print(cadena)