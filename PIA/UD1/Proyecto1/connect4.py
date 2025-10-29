import pygame
import sys
import numpy as np

# CONSTANTES DEL JUEGO
ROWS = 6 # Filas
COLS = 7 # Columnas
SQUARE_SIZE = 100 # Tamaño de cada cuadrado
RADIUS = int(SQUARE_SIZE / 2 - 5) # Radio de las fichas


BOARD_WIDTH = COLS * SQUARE_SIZE
MARGIN_X = 100  # Margen horizontal para centrar
WIDTH = BOARD_WIDTH + 2 * MARGIN_X # Ancho de la ventana
HEIGHT = (ROWS + 1) * SQUARE_SIZE # Alto de la ventana
SIZE = (WIDTH, HEIGHT) # Tamaño de la ventana

# Colores del juego
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

class Board:
    def __init__(self):
        self.board = np.zeros((ROWS, COLS))
        self.game_over = False
        self.turn = 0  # 0 para jugador 1, 1 para jugador 2
        
    def drop_piece(self, row, col, piece):
        """Coloca una ficha en el tablero"""
        self.board[row][col] = piece
        
    def is_valid_location(self, col):
        """Verifica si una columna es válida para colocar ficha"""
        return self.board[0][col] == 0
    
    def get_next_open_row(self, col):
        """Obtiene la siguiente fila disponible en una columna"""
        for r in range(ROWS - 1, -1, -1):
            if self.board[r][col] == 0:
                return r
        return -1
    
    def winning_move(self, piece):
        """Verifica si hay un movimiento ganador"""
        # Verificar horizontal
        for c in range(COLS - 3):
            for r in range(ROWS):
                if (self.board[r][c] == piece and 
                    self.board[r][c+1] == piece and 
                    self.board[r][c+2] == piece and 
                    self.board[r][c+3] == piece):
                    return True
        
        # Verificar vertical
        for c in range(COLS):
            for r in range(ROWS - 3):
                if (self.board[r][c] == piece and 
                    self.board[r+1][c] == piece and 
                    self.board[r+2][c] == piece and 
                    self.board[r+3][c] == piece):
                    return True
        
        # Verificar diagonal positiva
        for c in range(COLS - 3):
            for r in range(ROWS - 3):
                if (self.board[r][c] == piece and 
                    self.board[r+1][c+1] == piece and 
                    self.board[r+2][c+2] == piece and 
                    self.board[r+3][c+3] == piece):
                    return True
        
        # Verificar diagonal negativa
        for c in range(COLS - 3):
            for r in range(3, ROWS):
                if (self.board[r][c] == piece and 
                    self.board[r-1][c+1] == piece and 
                    self.board[r-2][c+2] == piece and 
                    self.board[r-3][c+3] == piece):
                    return True
        
        return False
    
    def is_board_full(self):
        """Verifica si el tablero está lleno"""
        return not any(0 in row for row in self.board)
    
    def make_move(self, col):
        """Realiza un movimiento en el tablero"""
        if self.game_over:
            return False
            
        if self.is_valid_location(col):
            row = self.get_next_open_row(col)
            if row != -1:
                piece = 1 if self.turn == 0 else 2
                self.drop_piece(row, col, piece)
                return row 
        return -1

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SIZE)
        pygame.display.set_caption("4 en Raya")
        self.clock = pygame.time.Clock()
        self.board = Board()
        self.font = pygame.font.SysFont("monospace", 75)
        self.animating = False
        self.animation_row = 0
        self.animation_col = 0
        self.animation_piece = 0
        self.animation_progress = 0
        
    def animate_piece(self, col, row, piece):
        """Anima la caída de una ficha"""
        self.animating = True
        self.animation_col = col
        self.animation_row = row
        self.animation_piece = piece
        self.animation_progress = 0
        
        # Animación: la ficha cae desde la parte superior
        while self.animation_progress <= row:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.draw_board_animation()
            self.animation_progress += 0.2  # Velocidad de la animación
            self.clock.tick(60)
        
        # Asegurarse de que la ficha termine en la posición correcta
        self.animation_progress = row
        self.draw_board_animation()
        self.animating = False
        
    def draw_board_animation(self):
        """Dibuja el tablero durante la animación"""
        self.screen.fill(BLUE)
        
        # Dibujar espacios vacíos (centrados horizontalmente)
        for c in range(COLS):
            for r in range(ROWS):
                pygame.draw.circle(self.screen, BLACK, (int(c * SQUARE_SIZE + SQUARE_SIZE / 2 + MARGIN_X), int(r * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)
        
        # Dibujar fichas existentes (centradas horizontalmente)
        for c in range(COLS):
            for r in range(ROWS):
                if self.board.board[r][c] == 1:  # Jugador 1
                    pygame.draw.circle(self.screen, RED, (int(c * SQUARE_SIZE + SQUARE_SIZE / 2 + MARGIN_X), int(r * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)
                elif self.board.board[r][c] == 2:  # Jugador 2
                    pygame.draw.circle(self.screen, YELLOW, (int(c * SQUARE_SIZE + SQUARE_SIZE / 2 + MARGIN_X), int(r * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)
        
        # Dibujar ficha en animación (centrada horizontalmente)
        if self.animating:
            color = RED if self.animation_piece == 1 else YELLOW
            y_pos = int(self.animation_progress * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE / 2)
            pygame.draw.circle(self.screen, color, (int(self.animation_col * SQUARE_SIZE + SQUARE_SIZE / 2 + MARGIN_X), y_pos), RADIUS)
        
        # Dibujar ficha flotante para mostrar el turno (solo si no hay animación)
        if not self.animating and not self.board.game_over:
            mouse_x = pygame.mouse.get_pos()[0]
            # Limitar la ficha flotante al área del tablero
            if MARGIN_X <= mouse_x <= MARGIN_X + BOARD_WIDTH:
                if self.board.turn == 0:
                    pygame.draw.circle(self.screen, RED, (mouse_x, int(SQUARE_SIZE / 2)), RADIUS)
                else:
                    pygame.draw.circle(self.screen, YELLOW, (mouse_x, int(SQUARE_SIZE / 2)), RADIUS)
        
        pygame.display.update()
    
    def draw_board(self):
        """Dibuja el tablero normal"""
        # Fondo azul
        self.screen.fill(BLUE)
        
        # Dibujar espacios vacíos (centrados horizontalmente)
        for c in range(COLS):
            for r in range(ROWS):
                pygame.draw.circle(self.screen, BLACK, (int(c * SQUARE_SIZE + SQUARE_SIZE / 2 + MARGIN_X), int(r * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)
        
        # Dibujar fichas (centradas horizontalmente)
        for c in range(COLS):
            for r in range(ROWS):
                if self.board.board[r][c] == 1:  # Jugador 1
                    pygame.draw.circle(self.screen, RED, (int(c * SQUARE_SIZE + SQUARE_SIZE / 2 + MARGIN_X), int(r * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)
                elif self.board.board[r][c] == 2:  # Jugador 2
                    pygame.draw.circle(self.screen, YELLOW, (int(c * SQUARE_SIZE + SQUARE_SIZE / 2 + MARGIN_X), int(r * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)
        
        # Dibujar ficha flotante para mostrar el turno
        if not self.board.game_over:
            mouse_x = pygame.mouse.get_pos()[0]
            # Limitar la ficha flotante al área del tablero
            if MARGIN_X <= mouse_x <= MARGIN_X + BOARD_WIDTH:
                if self.board.turn == 0:
                    pygame.draw.circle(self.screen, RED, (mouse_x, int(SQUARE_SIZE / 2)), RADIUS)
                else:
                    pygame.draw.circle(self.screen, YELLOW, (mouse_x, int(SQUARE_SIZE / 2)), RADIUS)
        
        pygame.display.update()
    
    def show_winner_message(self, winner):
        """Muestra el mensaje del ganador"""
        if winner == 1:
            label = self.font.render("¡Jugador 1 gana!", 1, RED)
        elif winner == 2:
            label = self.font.render("¡Jugador 2 gana!", 1, YELLOW)
        else:
            label = self.font.render("¡Empate!", 1, WHITE)
        
        # Centrar el mensaje horizontalmente
        label_x = WIDTH // 2 - label.get_width() // 2
        self.screen.blit(label, (label_x, 10))
        pygame.display.update()
        pygame.time.wait(2000)  # Esperar 2 segundos antes de preguntar por reinicio
    
    def handle_events(self):
        """Maneja los eventos del juego"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.MOUSEBUTTONDOWN and not self.board.game_over and not self.animating:
                # Obtener columna del click (ajustando por el margen)
                posx = event.pos[0]
                # Solo procesar clicks dentro del área del tablero
                if MARGIN_X <= posx <= MARGIN_X + BOARD_WIDTH:
                    col = (posx - MARGIN_X) // SQUARE_SIZE
                    
                    # Realizar movimiento
                    if 0 <= col < COLS:
                        row = self.board.make_move(col)
                        if row != -1:
                            # Animar la caída de la ficha
                            piece = 1 if self.board.turn == 0 else 2
                            self.animate_piece(col, row, piece)
                            
                            # Verificar si hay ganador después de la animación
                            if self.board.winning_move(piece):
                                self.board.game_over = True
                                self.show_winner_message(piece)
                                return True
                            
                            # Verificar empate
                            if self.board.is_board_full():
                                self.board.game_over = True
                                self.show_winner_message(0)  # 0 para empate
                                return True
                            
                            # Cambiar turno solo si no hay ganador
                            self.board.turn = 1 - self.board.turn
        
        return True
    
    def reset_game(self):
        """Reinicia el juego"""
        self.board = Board()
        self.animating = False
    
    def run(self):
        """Bucle principal del juego"""
        running = True
        while running:
            running = self.handle_events()
            
            if not self.animating:
                self.draw_board()
            
            self.clock.tick(60)
            
            # Si el juego terminó, preguntar si reiniciar
            if self.board.game_over and not self.animating:
                if not self.ask_restart():
                    running = False
        
        pygame.quit()
        sys.exit()
    
    def ask_restart(self):
        """Pregunta al usuario si quiere reiniciar el juego"""
        restart_font = pygame.font.SysFont("monospace", 50)
        label = restart_font.render("¿Jugar otra vez? (S/N)", 1, WHITE)
        
        overlay = pygame.Surface(SIZE)
        overlay.set_alpha(180)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))
        
        # Dibujar texto
        text_rect = label.get_rect(center=(WIDTH//2, HEIGHT//2))
        self.screen.blit(label, text_rect)
        pygame.display.update()
        
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        self.reset_game()
                        return True  # Continuar ejecución
                    elif event.key == pygame.K_n:
                        return False  # Salir del juego

if __name__ == "__main__":
    game = Game()
    game.run()