import random


class Tablero:
  def __init__(self, length):
    self._board = [[0 for _ in range(length)] for _ in range(length)]


  def dibujar_tablero(self):
    long = len(self._board)
    for i, fila in enumerate(self._board):
      print(" | ".join(str(cell) if cell != 0 else " " for cell in fila))
      if i < long - 1:
        print("-" * (long * 4 - 3))


  def get_board(self):
    return self._board


  def colocar_pieza(self, fila, columna, pieza):
    if fila >= len(self._board) or columna >= len(self._board[0]):
      return False
    if self._board[fila][columna] != 0:
      return False
    
    self._board[fila][columna] = pieza
    return True


class Juego:
  def __init__(self, length=3):
    self.tablero = Tablero(length)
    self.tablero.dibujar_tablero()

  def minimax(self, tablero):
      fila, columna = random.randint(0, 2), random.randint(0, 2)
      while not tablero.colocar_pieza(fila, columna, "O"):
          fila, columna = random.randint(0, 2), random.randint(0, 2)

  def hacer_jugada(self, turno):
    
    if turno == 1:
      jugador = "X" # Humano
      print("\nTu turno.")
      coordenadas = input("Introduce fila y columna separadas por coma (ejemplo: 1,2): ")
      fila, columna = map(int, coordenadas.split(","))
      
      while not self.tablero.colocar_pieza(fila - 1, columna - 1, jugador):
        coordenadas = input("No se puede colocar ahí. Introduce fila y columna separadas por coma (ejemplo: 1,2): ")
        fila, columna = map(int, coordenadas.split(","))
        
    elif turno == 2:
      jugador = "O" #IA
      print("\nTurno de la máquina...")
      self.minimax(self.tablero)
      
    self.tablero.dibujar_tablero()

  def fin_juego(self):
    tablero = self.tablero.get_board()
    long = len(tablero)
    
    for fila in tablero:
      if fila.count(fila[0]) == long and fila[0] != 0:
        print(f"\nGana el jugador {fila[0]}")
        return True
      
    for col in range(long):
      columna = [tablero[fila][col] for fila in range(long)]
      if columna.count(columna[0]) == long and columna[0] != 0:
        print(f"\nGana el jugador {columna[0]}")
        return True
    
    # Diagonal /
    diagonal = [tablero[i][i] for i in range(long)]
    if diagonal.count(diagonal[0]) == long and diagonal[0] != 0:
      print(f"\nGana el jugador {diagonal[0]}")
      return True
    
    # Diagonal \
    diagonal = [tablero[i][long - 1 - i] for i in range(long)]
    if diagonal.count(diagonal[0]) == long and diagonal[0] != 0:
      print(f"\nGana el jugador {diagonal[0]}")
      return True
    
    if all(celda != 0 for fila in tablero for celda in fila):
      print(f"\nEmpate")
      return True

    return False


  def jugar(self):
    turno = random.randint(1, 2)
    while not self.fin_juego():
      self.hacer_jugada(turno)
      turno = 2 if turno == 1 else 1


if __name__ == "__main__":
  juego = Juego()
  juego.jugar()