# Escribe un programa que pida una contraseña al usuario. La contraseña debe cumplir los siguientes requisitos:
  # Tener al menos 8 caracteres.
  # Contener al menos una letra mayúscula.
  # Contener al menos un número.

passwd = input("Introduzca su contraseña: ")

if len(passwd) < 8:
  print("La contraseña debe tener más de 8 caracteres.")
elif not any(c.isupper() for c in passwd):
  print("La contraseña debe contener al menos una letra mayúscula.")
elif not any(c.isdigit() for c in passwd):
  print("La contraseña debe contener al menos un número.")
else:
  print("La contraseña es válida.")