import random

intentos = 2000000

todas_negras = 0;

bolas = ["B"] * 7 + ["N"] * 5

for _ in range(intentos):
    muestra = random.sample(bolas, 4)
    if all(b == "N" for b in muestra):
        todas_negras += 1

print(f"Ha salido todas negras {todas_negras} veces. {todas_negras}/{intentos} = {((todas_negras / intentos) * 100):.2f}%")