"""Main module to run the program."""
from itertools import permutations


def solve_sudoku(board: list[list[int]]) -> list[list[int]]:
    """Solves the board"""
    return board


def lista_com_elementos_repetidos(números: list[list[int]]) -> bool:
    return not len(números) != len(set(números))

def is_valid(board: list[list[int]]) -> bool:
    """Checks if the board is valid"""
    #1. Criar uma lista com os elementos de cada linha e ver se eles estão repetidos
    for linha in board:
        linha_aux = [x for x in linha_aux if x != 0]
        if lista_com_elementos_repetidos(linha):
            return False
    #1.Criar uma lista com os elementos de cada coluna e ver se eles estão repetidos
    for j in range(len(board)):
        coluna = [linha[j] for linha in board]
        if lista_com_elementos_repetidos(coluna):
            return False
    #Criar uma lista com os elementos de cada diagonal e ver se eles estão repetidos
    diagonal_1 = [board[0][0], board[1][1], board[2][2]]
    diagonal_2 = [board[0][-1], board[1][-2], board[2][-3]]
    for diagonal in [diagonal_1, diagonal_2]:
        if lista_com_elementos_repetidos(diagonal):
            return False
    if len(board) != 9:
        return False
    return True

def testa_tudo():
    #Criar uma lista com todos os possíveis elementos
    possibilidades = [1, 1, 1, 2, 2, 2, 3, 3, 3]
    for tentativa in permutations(possibilidades):
        print(tentativa)