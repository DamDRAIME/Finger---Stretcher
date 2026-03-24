# https://leetcode.com/problems/valid-sudoku/

# Determine if a 9 x 9 Sudoku board is valid.


def isValidSudoku(board: list[list[str]]) -> bool:
    return are_columns_valid(board) and are_rows_valid(board) and are_squares_valid(board)


def are_columns_valid(board: list[list[str]]) -> bool:
    for x in range(9):
        column = [board[y][x] for y in range(9)]
        if contains_duplicate(column):
            return False
    return True


def are_rows_valid(board: list[list[str]]) -> bool:
    for row in board:
        if contains_duplicate(row):
            return False
    return True


def are_squares_valid(board: list[list[str]]) -> bool:
    for x in [1, 4, 7]:
        for y in [1, 4, 7]:
            square = []
            for x_offset in [-1, 0, 1]:
                for y_offset in [-1, 0, 1]:
                    square.append(board[y + y_offset][x + x_offset])
            if contains_duplicate(square):
                return False
    return True


def contains_duplicate(elements: list[str], exclude: str = ".") -> bool:
    seen = set()
    for el in elements:
        if el == exclude:
            continue
        if el in seen:
            return True
        seen.add(el)
    return False
