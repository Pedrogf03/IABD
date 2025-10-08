# Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10). A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor.

notas = []

for i in range(5):
  nota = float(input("Introduce una nota (0-10): "))
  while nota < 0 or nota > 10:
    print("Nota inválida. Debe estar entre 0 y 10.")
    nota = float(input("Introduce una nota (0-10): "))
  notas.append(nota)

print("Notas:", notas)
print("Nota media:", sum(notas)/len(notas))
print("Nota más alta:", max(notas))
print("Nota más baja:", min(notas))