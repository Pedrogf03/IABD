import random

num_equipos = int(input("Introduce el número de equipos: "))

equipos = []
resultados = []

for i in range(num_equipos):
  equipo = input("Introduce el nombre del equipo %d: " % (i+1))
  equipos.append(equipo)

partidos = []

n = len(equipos) 
for i in range(n): 
  for j in range(n): 
    if i != j: # evitar que un equipo juegue contra sí mismo 
      partidos.append((equipos[i], equipos[j]))

random.shuffle(partidos)

for partido in partidos:
  equipo1, equipo2 = partido
  goles1 = random.randint(0, 5)
  goles2 = random.randint(0, 5)
  resultados.append((equipo1, goles1, equipo2, goles2))

for resultado in resultados:
  equipo1, goles1, equipo2, goles2 = resultado
  print("%s %d - %d %s" % (equipo1, goles1, goles2, equipo2))



