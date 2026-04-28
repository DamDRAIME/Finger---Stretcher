# https://leetcode.com/problems/n-queens

# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each
# other. Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any
# order.

from collections import defaultdict

n = 0
solutions = []


def solveNQueens(n_queens: int) -> list[list[str]]:
    global n
    global solutions
    n = n_queens
    col_constraints = defaultdict(bool)
    diag_constraints = defaultdict(bool)
    idiag_constraints = defaultdict(bool)
    board = [["."] * n for _ in range(n)]
    solve(n, board, col_constraints, diag_constraints, idiag_constraints)
    return solutions


def solve(
    n_queens: int, board: list[list[str]], c_c: dict[int, bool], d_c: dict[int, bool], id_c: dict[int, bool]
) -> None:
    if n == 0:
        global solutions
        solutions.append(["".join(row) for row in board])
        return

    global n
    y = n - n_queens
    for x, el in enumerate(board[y]):
        if is_valid_pos(y, x, c_c, d_c, id_c):
            board[y][x] = "Q"
            c_c[x] = True
            d_c[(y - x) + (n - 1)] = True
            id_c[(y - (n - 1 - x)) + (n - 1)] = True
            solve(n - 1, board, c_c, d_c, id_c)
            c_c[x] = False
            d_c[(y - x) + (n - 1)] = False
            id_c[(y - (n - 1 - x)) + (n - 1)] = False
            board[y][x] = "."


def is_valid_pos(y: int, x: int, c_c: dict[int, bool], d_c: dict[int, bool], id_c: dict[int, bool]):
    return not (c_c[x] or d_c[(y - x) + (n - 1)] or id_c[(y - (n - 1 - x)) + (n - 1)])
