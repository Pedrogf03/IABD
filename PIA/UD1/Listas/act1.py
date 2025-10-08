# Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.

import random

nums = [random.randint(1,10) for _ in range(10)]
  
for num in nums:
  print(str(num) + " - " + str(num**2) + " - " + str(num**3))