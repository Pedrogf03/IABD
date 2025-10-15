import random

tiros = 1000000
caras = 0
cruces = 0

for tiro in range(tiros):
  num = random.randint(1,2)
  if num == 1:
    caras +=1
  elif num == 2:
    cruces +=1

print(f"Ha salido cara {caras} veces. {caras}/{tiros} = {caras / tiros}")
print(f"Ha salido cruz {cruces} veces. {cruces}/{tiros} = {cruces / tiros}")