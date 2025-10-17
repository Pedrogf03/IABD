import random

intentos = 2000000

todas_negras = 0;

for _ in range(intentos):
    bolas = ["B"] * 7 + ["N"] * 5
    muestra = random.sample(bolas, 4)
    if all(b == "N" for b in muestra):
        todas_negras += 1

print(f"Ha salido todas negras {todas_negras} veces. {todas_negras}/{intentos} = {todas_negras / intentos}")