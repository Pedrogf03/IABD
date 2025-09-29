# Programa que declare tres listas ‘lista1’, ‘lista2’ y ‘lista3’ de cinco enteros cada uno, pida valores para ‘lista1’ y ‘lista2’ y calcule lista3=lista1+lista2.

lista1 = []
lista2 = []

for i in range(5):
  num1 = int(input(f"Introduce el número {i+1} para la lista 1: "))
  lista1.append(num1)

for i in range(5):
  num2 = int(input(f"Introduce el número {i+1} para la lista 2: "))
  lista2.append(num2)
  
lista3 = [lista1[i] + lista2[i] for i in range(5)]

print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Lista 3 (suma de lista 1 y lista 2):", lista3)