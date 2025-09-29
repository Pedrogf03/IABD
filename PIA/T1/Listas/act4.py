# Programa que declare una lista y la vaya llenando de números hasta que introduzcamos un número negativo. Entonces se debe imprimir el vector (sólo los elementos introducidos). 

numeros = []

num = 0

while num >= 0:
  num = float(input("Introduce un número (negativo para terminar): "))
  if num >= 0:
    numeros.append(num)

print("Números introducidos:", numeros)
