# main.py
import pygame
import sys
from generate_sudoku import generate_sudoku
from solve_sudoku import solve_sudoku

# Constants
GRID_SIZE = 9
WINDOW_SIZE = 540
CELL_SIZE = WINDOW_SIZE // GRID_SIZE

filled_cells = []

# Initialize Pygame
pygame.init()
window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Sudoku Solver")

# Function to draw the Sudoku board
def draw_board(board):
    window.fill((255, 255, 255))
    
    # Draw the main grid lines
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            x = j * CELL_SIZE
            y = i * CELL_SIZE
            pygame.draw.rect(window, (0, 0, 0), (x, y, CELL_SIZE, CELL_SIZE), 1)
            if board[i][j] != 0:
                font = pygame.font.SysFont(None, 40)
                
                text = font.render(str(board[i][j]), True, (0, 0, 0))
                
                text_rect = text.get_rect(center=(x + CELL_SIZE // 2, y + CELL_SIZE // 2))
                window.blit(text, text_rect)

    # Draw thicker borders for 3x3 sub-grids
    for i in range(0, GRID_SIZE, 3):
        for j in range(0, GRID_SIZE, 3):
            x = j * CELL_SIZE
            y = i * CELL_SIZE
            pygame.draw.rect(window, (0, 0, 0), (x, y, CELL_SIZE * 3, CELL_SIZE * 3), 3)
     
    pygame.display.update()


# Main function
def main():
    sudoku_board = generate_sudoku()
    window.fill((255, 255, 255))
    draw_board(sudoku_board)
    pygame.display.update()

    # append the position of cells which are filled
    for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if(sudoku_board[i][j] != 0):
                    filled_cells.append((i,j))

    if solve_sudoku(sudoku_board):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                    sys.exit()
            # draw the solved sudoku
            for i in range(GRID_SIZE):
                for j in range(GRID_SIZE):
                    font = pygame.font.SysFont(None, 40)
                    # if number is the solution
                    if (i,j) not in filled_cells:
                        text = font.render(str(sudoku_board[i][j]), True, (255, 0, 0))
                        text_rect = text.get_rect(center=(j * CELL_SIZE + CELL_SIZE // 2, i * CELL_SIZE + CELL_SIZE // 2))
                        window.blit(text, text_rect)
                    pygame.display.update()
                    pygame.time.delay(50)

    
# Run the main function
if __name__ == "__main__":
    main()
