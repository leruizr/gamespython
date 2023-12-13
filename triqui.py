import pygame
import random

# Inicializar Pygame
pygame.init()

# Definir el tamaño de la ventana
width = 300
height = 300
window_size = (width, height)

# Crear la ventana
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Triqui")

# Variables para el juego
board = [['', '', ''],
         ['', '', ''],
         ['', '', '']]
current_player = 'X'

# Función para dibujar el tablero en la ventana
def draw_board():
    window.fill((255, 255, 255))  # Color de fondo

    # Dibujar líneas verticales
    pygame.draw.line(window, (0, 0, 0), (width // 3, 0), (width // 3, height), 2)
    pygame.draw.line(window, (0, 0, 0), (2 * width // 3, 0), (2 * width // 3, height), 2)

    # Dibujar líneas horizontales
    pygame.draw.line(window, (0, 0, 0), (0, height // 3), (width, height // 3), 2)
    pygame.draw.line(window, (0, 0, 0), (0, 2 * height // 3), (width, 2 * height // 3), 2)

    # Dibujar las fichas en el tablero
    for row in range(3):
        for col in range(3):
            if board[row][col] == 'X':
                pygame.draw.line(window, (255, 0, 0), (col * width // 3, row * height // 3),
                                 ((col + 1) * width // 3, (row + 1) * height // 3), 2)
                pygame.draw.line(window, (255, 0, 0), ((col + 1) * width // 3, row * height // 3),
                                 (col * width // 3, (row + 1) * height // 3), 2)
            elif board[row][col] == 'O':
                pygame.draw.circle(window, (0, 0, 255), ((col + 0.5) * width // 3, (row + 0.5) * height // 3),
                                   width // 6, 2)

    # Actualizar la ventana
    pygame.display.flip()

# Función para verificar si alguien ha ganado
def check_win():
    # Verificar filas
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != '':
            return True

    # Verificar columnas
    for col in range(len(board[0])):
        check = []
        for row in board:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != '':
            return True

    # Verificar diagonales
    if board[0][0] == board[1][1] == board[2][2] != '':
        return True
    if board[0][2] == board[1][1] == board[2][0] != '':
        return True

    return False

# Función para la jugada de la computadora
def computer_move():
    move_made = False
    while not move_made:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == '':
            board[row][col] = 'O'
            move_made = True

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and current_player == 'X':
            # Obtener la posición del clic del mouse
            pos = pygame.mouse.get_pos()

            # Calcular la fila y columna correspondiente
            row = pos[1] // (height // 3)
            col = pos[0] // (width // 3)

            # Verificar si la casilla está vacía
            if board[row][col] == '':
                # Colocar la ficha del jugador actual en la casilla
                board[row][col] = current_player

                # Cambiar al siguiente jugador
                if current_player == 'X':
                    current_player = 'O'
                else:
                    current_player = 'X'

                # Dibujar el tablero actualizado
                draw_board()

                # Verificar si alguien ha ganado
                if check_win():
                    print("¡El jugador X ha ganado!")
                    running = False

    # Jugada de la computadora
    if current_player == 'O' and running:
        computer_move()
        current_player = 'X'
        draw_board()
        if check_win():
            print("¡La computadora ha ganado!")
            running = False

# Finalizar Pygame
pygame.quit()