# Escribe un programa que pida una palabra al usuario y verifique si es un palíndromo (se lee igual hacia adelante que hacia atrás).

palabra = input("Introduce una palabra: ")

palabra = palabra.strip().lower()
es_palindromo = True

for i in range(len(palabra) // 2):
  if palabra[i] != palabra[-(i+1)]:
    es_palindromo = False
    break

if es_palindromo:
  print("La palabra es un palíndromo.")
else:
  print("La palabra NO es un palíndromo.")
