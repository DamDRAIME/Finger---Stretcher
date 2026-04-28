# https://leetcode.com/problems/n-queens

# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each
# other. Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any
# order.

from copy import deepcopy
from collections import defaultdict

solutions = []
n = 0


def solveNQueens(n_queens: int) -> list[list[str]]:
    global n
    global solutions
    n = n_queens
    row_constraints = defaultdict(int)
    col_constraints = defaultdict(int)
    diag_constraints = defaultdict(int)
    idiag_constraints = defaultdict(int)
    board = [["?"] * n for _ in range(n)]
    solve(n, board, row_constraints, col_constraints, diag_constraints, idiag_constraints)
    return solutions


def solve(n, board, r_c, c_c, d_c, id_c) -> None:
    if n == 0:
        global solutions
        solutions.append(["".join(row).replace("?", ".") for row in board])
        return

    for y, row in enumerate(board):
        for x, el in enumerate(row):
            if el == "?":
                if is_valid_pos(y, x, r_c, c_c, d_c, id_c):
                    temp_board = deepcopy(board)
                    temp_board[y][x] = "Q"
                    solve(n - 1, temp_board, *update_constraints(y, x, r_c, c_c, d_c, id_c))
                board[y][x] = "."


def is_valid_pos(y, x, r_c, c_c, d_c, id_c):
    global n
    return not (r_c[x] or c_c[y] or d_c[(y - x) + (n - 1)] or id_c[(y - (n - 1 - x)) + (n - 1)])


def update_constraints(y, x, r_c, c_c, d_c, id_c):
    global n
    r_c = deepcopy(r_c)
    r_c[x] = 1
    c_c = deepcopy(c_c)
    c_c[y] = 1
    d_c = deepcopy(d_c)
    d_c[(y - x) + (n - 1)] = 1
    id_c = deepcopy(id_c)
    id_c[(y - (n - 1 - x)) + (n - 1)] = 1
    return r_c, c_c, d_c, id_c
