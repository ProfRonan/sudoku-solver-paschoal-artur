def lista_com_elementos_repetidos(números: list[int]) -> bool:
    números = [x for x in números if x != 0]
    return len(números) != len(set(números))

def solve_sudoku(board: list[list[int]]) -> list[list[int]]:
    """Solves the board"""
    celula_vazia = find_célula_vazia(board)
    if celula_vazia is None:
        return True

    i, j = célula_vazia

    for num in range(1,10):
        if is_valid(board, i, j, num):
            board[i][j] = num
            if solve_sudoku(board):
                return board
            board[i][j] = 0
    raise ValueError

def is_valid(board, num, i, j: list[list[int]]) -> bool:
    for x in range(9):
        # Check row
        if board[i][x] == num:
            return False
        # Check column
        if board[x][j] == num:
            return False
    # Check subgrid
    start_row = (i // 3) * 3
    start_col = (j // 3) * 3
    for row in range(start_row, start_row + 3):
        for col in range(start_col, start_col + 3):
            if board[row][col] == num:
                return False
    return True

def find_empty_cell(board: list[list[int]]) -> bool:
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def is_full(tabuleiro):
#verifica se o tabuleiro tem casas não preenchidas
  for linha in tabuleiro:
    for elemento in linha:
      if elemento == 0:
        return False
  return True

def still_can_play(possibilidades):
    for linha in possibilidades:
        for opções in linha:
            if not opções:
                return True
    return False