import random

tiros = 1000000
rojos = 0
negros = 0
verdes = 0

for tiro in range(tiros):
  num = random.randint(0,37)
  if num == 0:
    verdes += 1
  elif num % 2 == 0:
    negros +=1
  elif not num % 2 == 0:
    rojos +=1

print(f"Ha salido rojo {rojos} veces. {rojos}/{tiros} = {rojos / tiros}")
print(f"Ha salido negro {negros} veces. {negros}/{tiros} = {negros / tiros}")
print(f"Ha salido verde {verdes} veces. {verdes}/{tiros} = {verdes / tiros}")