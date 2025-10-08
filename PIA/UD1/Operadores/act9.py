# Escribe un programa que pida la edad del usuario y determine en qué categoría se encuentra:
  # Niño: Menor de 12 años.
  # Adolescente: Entre 12 y 18 años.
  # Adulto: Mayor de 18 años.
  
edad = float(input("Introduzca su edad: "))

if 0 <= edad < 12:
  print("Eres un niño.")
elif edad <= 18:
  print("Eres un adolescente.")
elif 18 < edad:
  print("Eres un adulto.")
else:
  print("Esa edad no es válida.")
