
def solve_sudoku(board: list[list[int]]) -> list[list[int]]:
    empty_cell = find_empty_cell(board)
    if empty_cell is None:
        return board

    row, col = empty_cell
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return board

            board[row][col] = 0

    raise ValueError

def is_valid(board: list[list[int]], row: int, col: int, num: int) -> bool:
    for i in range(9):
        if board[row][i] == num and i != col:
            return False

    for i in range(9):
        if board[i][col] == num and i != row:
            return False

    start_row = 3 * (row // 3)
    start_col = 3 * (col // 3)

    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num and (i != row or j != col):
                return False

    return True


def find_empty_cell(board: list[list[int]]) -> tuple[int, int]:
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None