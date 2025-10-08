num = []

while True:
  
  print("\nMenú:")
  print("1. Añadir número a la lista")
  print("2. Añadir número de la lista en una posición")
  print("3. Longitud de la lista")
  print("4. Eliminar último número")
  print("5. Eliminar un número")
  print("6. Contar números")
  print("7. Posiciones de un número")
  print("8. Mostrar números")
  print("0. Salir")
  
  print(num)
  
  opcion = input("Elige una opción: ")
  
  if opcion == '0':
    print("Saliendo del programa.")
    break
  elif opcion == '1':
    numero = int(input("Introduce un número para añadir a la lista: "))
    num.append(numero)
    print(f"Número {numero} añadido a la lista.")
  elif opcion == '2':
    numero = int(input("Introduce un número para añadir a la lista: "))
    while True:
      posicion = int(input("Introduce la posición: ")) - 1
      if 0 <= posicion <= len(num):
        num.insert(posicion, numero)
        print(f"Número {numero} añadido en la posición {posicion}.")
        break
      else:
        print("Posición no válida.")
  elif opcion == '3':
    print(f"La longitud de la lista es: {len(num)}")
  elif opcion == '4':
    if num:
      ultimo_numero = num.pop()
      print(f"Número {ultimo_numero} eliminado de la lista.")
    else:
      print("La lista está vacía.")
  elif opcion == '5':
    if num:
      while True:
        posicion = int(input("Introduce la posición a eliminar: ")) - 1
        if 0 <= posicion < len(num):
          eliminado = num.pop(posicion)
          print(f"Número {eliminado} eliminado de la posición {posicion + 1}.")
          break
        else:
          print("Posición no válida.")
    else:
      print("La lista está vacía.")
  elif opcion == '6':
    numero = int(input("Introduce un número para contar sus apariciones: "))
    apariciones = num.count(numero)
    print(f"El número {numero} aparece {apariciones} veces en la lista.")
  elif opcion == '7':
    numero = int(input("Introduce un número para encontrar sus posiciones: "))
    posiciones = [i + 1 for i, x in enumerate(num) if x == numero]
    if posiciones:
      print(f"El número {numero} está en las posiciones: {posiciones}")
    else:
      print(f"El número {numero} no está en la lista.")
  elif opcion == '8':
    print("Números en la lista:", num)