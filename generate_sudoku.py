# generate_sudoku.py
import random
from solve_sudoku import solve_sudoku
board_SIZE = 9

def generate_sudoku():
    board = [[0] * 9 for _ in range(9)]
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Fill the diagonal 3x3 boards with random numbers
    for i in range(0, 9, 3):
        random.shuffle(numbers)
        for j in range(3):
            board[i + j][i + j] = numbers[j]
    

    # Solve the Sudoku
    solve_sudoku(board)

    # Remove some cells to create the puzzle
    num_cells_to_remove = random.randint(40, 55)

    for _ in range(num_cells_to_remove):
        while True:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            if board[row][col] != 0:
                board[row][col] = 0
                break

    return board



