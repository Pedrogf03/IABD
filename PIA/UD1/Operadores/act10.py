# Escribe un programa que simule una calculadora.
  # El programa debe pedir al usuario dos números y una operación (+, -, *, /) y realizar el cálculo correspondiente.
  
while True:
  # Pedir números al usuario
  try:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
  except ValueError:
    print("Por favor, introduce un número válido.")
    continue

  operacion = input("Introduce la operación (+, -, *, /): ")

  if operacion == '+':
    resultado = num1 + num2
  elif operacion == '-':
    resultado = num1 - num2
  elif operacion == '*':
    resultado = num1 * num2
  elif operacion == '/':
    if num2 != 0:
      resultado = num1 / num2
    else:
      print("Error: No se puede dividir entre cero.")
      continue
  else:
    print("Operación no válida. Intenta de nuevo.")
    continue

  print(f"Resultado: {resultado}")

  salir = input("Pulsa 's' para salir o cualquier otra tecla para continuar: ").lower()
  if salir == 's':
    print("Calculadora finalizada.")
    break
