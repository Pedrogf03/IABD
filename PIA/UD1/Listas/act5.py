# Hacer un programa que inicialice una lista de números con valores aleatorios (10 valores), y posterior ordene los elementos de menor a mayor. 

import random

numeros = [random.randint(1, 100) for _ in range(10)]

numeros.sort()

print("Números ordenados de menor a mayor:", numeros)