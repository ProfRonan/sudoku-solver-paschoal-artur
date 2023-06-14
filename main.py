def lista_com_elementos_repetidos(números: list[int]) -> bool:
    números = [x for x in números if x != 0]
    return len(números) != len(set(números))

def solve_sudoku(board: list[list[int]]) -> list[list[int]]:
    """Solves the board"""
    célula_vazia = find_célula_vazia(board)
    if célula_vazia is None:
        return True

    i, j = célula_vazia

    for num in range(1,10):
        if is_valid(board, i, j, num):
            board[i][j] = num
            if solve_sudoku(board):
                return board
            board[i][j] = 0
    raise ValueError

def is_valid(board: list[list[int]]) -> bool:
    """Checks if the board is valid"""
    for linha in board:
        if lista_com_elementos_repetidos(linha):
            return False
    for j in range(len(board)):
        coluna = [linha[j] for linha in board]
        if lista_com_elementos_repetidos(coluna):
            return False

def find_célula_vazia(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0
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