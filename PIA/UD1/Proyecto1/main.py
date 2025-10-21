import csv
import os

class Alumno:
  
  def __init__(self, nombre: str, apellidos):
    self.nombre = nombre
    self.apellidos = apellidos
    self.cursos = []
    
  def __eq__(self, otro):
    if not isinstance(otro, Alumno):
      return False
    return self.nombre == otro.nombre and self.apellidos == otro.apellidos
  
  def __repr__(self):
    return f"{self.nombre} {self.apellidos}"

# ---------------------------------------------------------------------------------------- #

class Curso:
  
  def __init__(self, nombre: str):
    self.nombre = nombre
    self.alumnos = []
  
  def __eq__(self, otro):
    if not isinstance(otro, Curso):
      return False
    return self.nombre == otro.nombre
  
  def __repr__(self):
    return f"{self.nombre}"
  
  # Método privado para que un curso inscriba a un alumno.
  def _inscribir_alumno(self, alumno: Alumno):
    if alumno in self.alumnos:
      print("Ese alumno ya está matriculado en este curso.")
      return
    self.alumnos.append(alumno)
    alumno.cursos.append(self)
    
  def remove(self, alumno: Alumno):
    if alumno in self.alumnos:
      self.alumnos.remove(alumno)

# ---------------------------------------------------------------------------------------- #

class Centro:
  
  def __init__(self, file: str = "centro.csv"):
    self.cursos = []
    self.alumnos = []
    
    if not os.path.exists(file):
      with open(file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(["tipo", "nombre", "apellidos", "cursos"])
        print("Archivo centro.csv creado.")
    else:
      with open(file, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=";")
        for fila in reader:
          if fila["tipo"].strip().lower() == "curso":
            nombre_curso = fila["nombre"].strip()
            curso = Curso(nombre_curso)
            self.cursos.append(curso)

        f.seek(0)
        reader = csv.DictReader(f, delimiter=";")
        for fila in reader:
          if fila["tipo"].strip().lower() == "alumno":
            nombre_alumno = fila["nombre"].strip()
            apellidos = fila["apellidos"].strip()
            alumno = Alumno(nombre_alumno, apellidos)
            self.alumnos.append(alumno)

            cursos_str = fila.get("cursos", "").strip()
            if cursos_str:
              nombres_cursos = [c.strip() for c in cursos_str.split(",")]
              for nombre_curso in nombres_cursos:
                nombre_curso = nombre_curso.strip()
                curso_obj = next((c for c in self.cursos if c.nombre == nombre_curso), None)
                if curso_obj:
                  curso_obj.alumnos.append(alumno)
                  alumno.cursos.append(curso_obj)

      print(f"Cargados {len(self.alumnos)} alumnos y {len(self.cursos)} cursos desde centro.csv.")

  def save(self, file: str = "centro.csv"):
    with open(file, "w", newline="", encoding="utf-8") as f:
      writer = csv.writer(f, delimiter=";")
      writer.writerow(["tipo", "nombre", "apellidos", "cursos"])
      
      for curso in self.cursos:
        writer.writerow(["curso", curso.nombre, "", ""])
      
      for alumno in self.alumnos:
        cursos_str = ",".join([curso.nombre for curso in alumno.cursos])
        writer.writerow(["alumno", alumno.nombre, alumno.apellidos, cursos_str])
    
    print(f"Datos guardados en {file}")
    
  # -- Gestión de Alumnos -- #

  # Método para añadir un alumno al centro.
  def add_alumno(self):
    nombre = input("Introduzca el nombre del alumno: ")
    apellidos = input("Introduzca los apellidos del alumno: ")
    
    alumno = Alumno(nombre, apellidos)
    
    if alumno in self.alumnos:
      print("Ya existe un alumno con ese nombre y apellidos.")
      return
    
    self.alumnos.append(alumno)
    print("Alumno añadido correctamente.")
  
  # Método para eliminar un alumno del centro.
  def remove_alumno(self, alumno: Alumno):
    if alumno not in self.alumnos:
      print("Ese alumno no está en nuestro centro.")
      return
    
    for curso in self.cursos:
      curso.remove(alumno)
      
    self.alumnos.remove(alumno)
    print("Alumno eliminado correctamente.")
      
  # Método para editar un alumno.
  def editar_alumno(self, alumno: Alumno):
    if alumno not in self.alumnos:
      print("Ese alumno no está en nuestro centro.")
      return

    nuevo_nombre = input("Introduzca el nuevo nombre del alumno: ")
    nuevos_apellidos = input("Introduzca los nuevos apellidos del alumno: ")
      
    alumno_temporal = Alumno(nuevo_nombre, nuevos_apellidos)

    if alumno_temporal in self.alumnos:
      print("Ese alumno ya existe.")
      return

    alumno.nombre = nuevo_nombre
    alumno.apellidos = nuevos_apellidos
    print("Alumno editado correctamente.")
  
  # Método para inscribir a un alumno en un curso.
  def inscribir_alumno_curso(self, alumno: Alumno, curso: Curso):
    if alumno not in self.alumnos:
      print("Ese alumno no está en nuestro centro.")
      return
    
    curso._inscribir_alumno(alumno)
    print(f"Alumno {alumno.nombre} matriculado correctamente en el curso de {curso.nombre}.")
  
  # -- Gestión de Cursos --
  
  # Método para añadir un curso al centro.
  def add_curso(self):
    nombre = input("Introduzca el nombre del curso: ")
    curso = Curso(nombre)
    
    if curso in self.cursos:
      print("Ya existe un curso con ese nombre.")
      return
    
    self.cursos.append(curso)
    print("Curso añadido correctamente.")
  
  # Método para eliminar un curso del centro.
  def remove_curso(self, curso: Curso):
    if curso not in self.cursos:
      print("Ese curso no está en nuestro centro.")
      return
    
    self.cursos.remove(curso)
    print("Curso eliminado correctamente.")
  
  # Método para editar un curso.
  def editar_curso(self, curso: Curso):
    if curso not in self.cursos:
      print("Ese curso no está en nuestro centro.")
      return

    nuevo_nombre = input("Introduzca el nuevo nombre del curso: ")
      
    curso_temporal = Curso(nuevo_nombre)

    if curso_temporal in self.cursos:
      print("Ya existe un curso con ese nombre.")
      return

    curso.nombre = nuevo_nombre
    print("Curso editado correctamente.")
  
  # -- CONSULTAS -- 
  
  # Alumnos de un curso
  def consultar_alumnos_curso(self, curso: Curso):
    if curso not in self.cursos:
      print("Ese curso no está en nuestro centro.")
      return
    
    if len(curso.alumnos) == 0:
      print("No hay alumnos matriculados en este curso.")
      return
    
    print(f"Los alumnos matriculados en el curso de {curso.nombre} son: ")
    for alumno in curso.alumnos:
      print(f"{alumno.nombre} {alumno.apellidos}")

  # Cursos de un alumno
  def consultar_cursos_alumno(self, alumno: Alumno):
    if alumno not in self.alumnos:
      print("Ese alumno no está en nuestro centro.")
      return
    
    if len(alumno.cursos) == 0:
      print("Este alumno no está matriculado en ningún curso.")
      return
      
    print(f"Los cursos en los que está matriculado el alumno {alumno.nombre} son: ")
    for curso in alumno.cursos:
      print(f"{curso.nombre}")

# ---------------------------------------------------------------------------------------- #

centro = Centro()

while True:
  pass

centro.save()