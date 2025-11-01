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


  def copiar(self):
    nuevo = Tablero(len(self._board))
    nuevo._board = [fila[:] for fila in self._board]
    return nuevo


class Juego:
  def __init__(self, length=3):
    self.tablero = Tablero(length)
    self.tablero.dibujar_tablero()


  def fin_juego(self, tablero=None):
    tablero = tablero or self.tablero.get_board()
    long = len(tablero)
    
    for fila in tablero:
      if fila.count(fila[0]) == long and fila[0] != 0:
        return fila[0]
      
    for col in range(long):
      columna = [tablero[fila][col] for fila in range(long)]
      if columna.count(columna[0]) == long and columna[0] != 0:
        return columna[0]
    
    # Diagonal /
    diagonal = [tablero[i][i] for i in range(long)]
    if diagonal.count(diagonal[0]) == long and diagonal[0] != 0:
      return diagonal[0]
    
    # Diagonal \
    diagonal = [tablero[i][long - 1 - i] for i in range(long)]
    if diagonal.count(diagonal[0]) == long and diagonal[0] != 0:
      return diagonal[0]
    
    if all(celda != 0 for fila in tablero for celda in fila):
      return "Empate"

    return None


  def minimax(self, tablero, es_maximizador):
    resultado = self.fin_juego(tablero.get_board())
    if resultado == "O":
      return 1
    elif resultado == "X":
      return -1
    elif resultado == "Empate":
      return 0
    
    if es_maximizador:
      mejor_valor = -float("inf")
      for i in range(len(tablero.get_board())):
        for j in range(len(tablero.get_board()[0])):
          if tablero.get_board()[i][j] == 0:
            copia = tablero.copiar()
            copia.colocar_pieza(i, j, "O")
            valor = self.minimax(copia, False)
            mejor_valor = max(mejor_valor, valor)
      return mejor_valor
    else:
      mejor_valor = float("inf")
      for i in range(len(tablero.get_board())):
        for j in range(len(tablero.get_board()[0])):
          if tablero.get_board()[i][j] == 0:
            copia = tablero.copiar()
            copia.colocar_pieza(i, j, "X")
            valor = self.minimax(copia, True)
            mejor_valor = min(mejor_valor, valor)
      return mejor_valor


  def mejor_jugada_ia(self):
    mejor_valor = -float("inf")
    mejor_mov = None
    
    for fila in range(len(self.tablero.get_board())):
      for columna in range(len(self.tablero.get_board()[0])):
        if self.tablero.get_board()[fila][columna] == 0:
          copia = self.tablero.copiar()
          copia.colocar_pieza(fila, columna, "O")
          valor = self.minimax(copia, False)
          if valor > mejor_valor:
            mejor_valor = valor
            mejor_mov = (fila, columna)
    
    if mejor_mov:
      fila, columna = mejor_mov
      self.tablero.colocar_pieza(fila, columna, "O")


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
      self.mejor_jugada_ia()
      
    self.tablero.dibujar_tablero()


  def jugar(self):
    turno = random.randint(1, 2)
    while True:
      ganador = self.fin_juego(self.tablero.get_board())
      if ganador:
        if ganador == "Empate":
          print("\nEmpate.")
        else:
          print(f"\nGana el jugador {ganador}")
        break
    
      self.hacer_jugada(turno)
      turno = 2 if turno == 1 else 1


if __name__ == "__main__":
  juego = Juego()
  juego.jugar()