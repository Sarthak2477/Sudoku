# solve_soduku.py
board_SIZE = 9
def solve_sudoku(board,depth=0, max_depth=1000):
    if depth > max_depth:
        raise RecursionError("Max recursion depth exceeded")
    
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True

    row, col = empty_cell

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board, depth + 1, max_depth):
                return True

            board[row][col] = 0

    return False

def is_valid(board, row, col, num):
     # Check row and column
    for i in range(board_SIZE):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check the 3x3 board
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def find_empty_cell(board):
    for i in range(board_SIZE):
        for j in range(board_SIZE):
            if board[i][j] == 0:
                return i, j
    return None