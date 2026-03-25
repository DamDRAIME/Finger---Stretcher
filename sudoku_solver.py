# https://leetcode.com/problems/sudoku-solver

# Write a program to solve a Sudoku puzzle by filling the empty cells.


from copy import deepcopy


def solveSudoku(board: list[list[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    new_board = solve(deepcopy(board))
    for y in range(9):
        board[y] = new_board[y]


def solve(board: list[list[str]]) -> None:
    cell = next_cell(board)
    if cell is None:
        return deepcopy(board)
    x, y = cell
    candidates = get_candidates(x, y, board)
    if not candidates:
        return None
    for candidate in candidates:
        board_ = deepcopy(board)
        board_[y][x] = candidate
        new_board = solve(deepcopy(board_))
        if new_board is None:
            continue
        return deepcopy(new_board)


def next_cell(board: list[list[str]]) -> tuple[int, int]:
    for y in range(9):
        for x in range(9):
            if board[y][x] == ".":
                return x, y
    return None


def get_candidates(x: int, y: int, board: list[list[str]]) -> list[str]:
    candidates = set([str(x) for x in range(1, 10)])
    candidates -= get_square_elements(x, y, board)
    candidates -= get_column_elements(x, board)
    candidates -= get_row_elements(y, board)
    return list(candidates)


def get_square_elements(x: int, y: int, board: list[list[str]]) -> set[str]:
    x = (x // 3) * 3
    y = (y // 3) * 3
    square = set()
    for x_offset in range(3):
        for y_offset in range(3):
            el = board[y + y_offset][x + x_offset]
            if el == ".":
                continue
            square.add(el)
    return square


def get_column_elements(x: int, board: list[list[str]]) -> set[str]:
    return set(board[y][x] for y in range(9) if board[y][x] != ".")


def get_row_elements(y: int, board: list[list[str]]) -> set[str]:
    return set(el for el in board[y] if el != ".")
