import csv
import os

class Alumno:
    def __init__(self, nombre: str, apellidos: str):
        self.nombre = nombre
        self.apellidos = apellidos
        self.cursos = []

    def __eq__(self, otro):
        return isinstance(otro, Alumno) and self.nombre.lower() == otro.nombre.lower() and self.apellidos.lower() == otro.apellidos.lower()

    def __repr__(self):
        return f"{self.nombre} {self.apellidos}"


class Curso:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.alumnos = []

    def __eq__(self, otro):
        return isinstance(otro, Curso) and self.nombre.lower() == otro.nombre.lower()

    def __repr__(self):
        return f"{self.nombre}"

    def _inscribir_alumno(self, alumno: Alumno):
        if alumno in self.alumnos:
            print("Ese alumno ya está matriculado en este curso.")
            return
        self.alumnos.append(alumno)
        alumno.cursos.append(self)


class Centro:
    def __init__(self, file: str = "centro.csv"):
        self.cursos = []
        self.alumnos = []
        self.file = file

        if not os.path.exists(file):
            with open(file, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f, delimiter=";")
                writer.writerow(["tipo", "nombre", "apellidos", "cursos"])
            print("Archivo centro.csv creado.")
        else:
            self.cargar(file)

    def cargar(self, file: str):
        with open(file, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter=";")

            # Primero cargamos los cursos
            for fila in reader:
                if fila["tipo"].strip().lower() == "curso":
                    self.cursos.append(Curso(fila["nombre"].strip()))

        with open(file, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter=";")

            # Luego cargamos los alumnos y sus cursos
            for fila in reader:
                if fila["tipo"].strip().lower() == "alumno":
                    alumno = Alumno(fila["nombre"].strip(), fila["apellidos"].strip())
                    self.alumnos.append(alumno)

                    cursos_str = fila.get("cursos", "").strip()
                    if cursos_str:
                        nombres_cursos = [c.strip() for c in cursos_str.split(",")]
                        for nombre_curso in nombres_cursos:
                            curso_obj = next((c for c in self.cursos if c.nombre.lower() == nombre_curso.lower()), None)
                            if curso_obj:
                                curso_obj.alumnos.append(alumno)
                                alumno.cursos.append(curso_obj)

        print(f"Cargados {len(self.alumnos)} alumnos y {len(self.cursos)} cursos desde {file}.")

    def save(self):
        with open(self.file, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow(["tipo", "nombre", "apellidos", "cursos"])

            for curso in self.cursos:
                writer.writerow(["curso", curso.nombre, "", ""])

            for alumno in self.alumnos:
                cursos_str = ",".join([curso.nombre for curso in alumno.cursos])
                writer.writerow(["alumno", alumno.nombre, alumno.apellidos, cursos_str])

        print(f"Datos guardados en {self.file}.")

    # ------------------- GESTIÓN DE ALUMNOS ------------------- #

    def add_alumno(self):
        nombre = input("Introduzca el nombre del alumno: ").strip()
        apellidos = input("Introduzca los apellidos del alumno: ").strip()
        alumno = Alumno(nombre, apellidos)

        if alumno in self.alumnos:
            print("Ya existe un alumno con ese nombre y apellidos.")
            return

        self.alumnos.append(alumno)
        print("Alumno añadido correctamente.")

    def editar_alumno(self):
        alumno = self._buscar_alumno()
        if not alumno:
            return

        nuevo_nombre = input("Nuevo nombre: ").strip()
        nuevos_apellidos = input("Nuevos apellidos: ").strip()
        alumno_temp = Alumno(nuevo_nombre, nuevos_apellidos)

        if alumno_temp in self.alumnos and alumno_temp != alumno:
            print("Ya existe otro alumno con ese nombre.")
            return

        alumno.nombre = nuevo_nombre
        alumno.apellidos = nuevos_apellidos
        print("Alumno editado correctamente.")

    def remove_alumno(self):
        alumno = self._buscar_alumno()
        if not alumno:
            return

        for curso in alumno.cursos:
            if alumno in curso.alumnos:
                curso.alumnos.remove(alumno)

        self.alumnos.remove(alumno)
        print("Alumno eliminado correctamente.")

    # ------------------- GESTIÓN DE CURSOS ------------------- #

    def add_curso(self):
        nombre = input("Introduzca el nombre del curso: ").strip()
        curso = Curso(nombre)

        if curso in self.cursos:
            print("Ya existe un curso con ese nombre.")
            return

        self.cursos.append(curso)
        print("Curso añadido correctamente.")

    def editar_curso(self):
        curso = self._buscar_curso()
        if not curso:
            return

        nuevo_nombre = input("Nuevo nombre del curso: ").strip()
        curso_temp = Curso(nuevo_nombre)

        if curso_temp in self.cursos and curso_temp != curso:
            print("Ya existe otro curso con ese nombre.")
            return

        curso.nombre = nuevo_nombre
        print("Curso editado correctamente.")

    def remove_curso(self):
        curso = self._buscar_curso()
        if not curso:
            return

        for alumno in self.alumnos:
            if curso in alumno.cursos:
                alumno.cursos.remove(curso)

        self.cursos.remove(curso)
        print("Curso eliminado correctamente.")

    # ------------------- INSCRIPCIONES ------------------- #

    def inscribir_alumno_curso(self):
        alumno = self._buscar_alumno()
        if not alumno:
            return

        curso = self._buscar_curso()
        if not curso:
            return

        curso._inscribir_alumno(alumno)
        print(f"Alumno {alumno.nombre} matriculado correctamente en {curso.nombre}.")

    # ------------------- CONSULTAS ------------------- #

    def consultar_alumnos_curso(self):
        curso = self._buscar_curso()
        if not curso:
            return

        if not curso.alumnos:
            print("No hay alumnos matriculados en este curso.")
            return

        print(f"\nAlumnos en {curso.nombre}:")
        for alumno in curso.alumnos:
            print(f"- {alumno.nombre} {alumno.apellidos}")

    def consultar_cursos_alumno(self):
        alumno = self._buscar_alumno()
        if not alumno:
            return

        if not alumno.cursos:
            print("Este alumno no está matriculado en ningún curso.")
            return

        print(f"\nCursos de {alumno.nombre} {alumno.apellidos}:")
        for curso in alumno.cursos:
            print(f"- {curso.nombre}")

    # ------------------- MÉTODOS AUXILIARES ------------------- #

    def _buscar_alumno(self):
        nombre = input("Nombre del alumno: ").strip()
        apellidos = input("Apellidos del alumno: ").strip()
        alumno = next((a for a in self.alumnos if a.nombre.lower() == nombre.lower() and a.apellidos.lower() == apellidos.lower()), None)
        if not alumno:
            print("Alumno no encontrado.")
        return alumno

    def _buscar_curso(self):
        nombre = input("Nombre del curso: ").strip()
        curso = next((c for c in self.cursos if c.nombre.lower() == nombre.lower()), None)
        if not curso:
            print("Curso no encontrado.")
        return curso


# ---------------------------------------------------------------------------------------- #

def menu():
    centro = Centro()

    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Añadir alumno")
        print("2. Editar alumno")
        print("3. Eliminar alumno")
        print("4. Añadir curso")
        print("5. Editar curso")
        print("6. Eliminar curso")
        print("7. Inscribir alumno en curso")
        print("8. Consultar alumnos de un curso")
        print("9. Consultar cursos de un alumno")
        print("0. Guardar y salir")

        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1": centro.add_alumno()
            case "2": centro.editar_alumno()
            case "3": centro.remove_alumno()
            case "4": centro.add_curso()
            case "5": centro.editar_curso()
            case "6": centro.remove_curso()
            case "7": centro.inscribir_alumno_curso()
            case "8": centro.consultar_alumnos_curso()
            case "9": centro.consultar_cursos_alumno()
            case "0":
                centro.save()
                print("¡Hasta pronto!")
                break
            case _:
                print("Opción no válida.")

if __name__ == "__main__":
    menu()
