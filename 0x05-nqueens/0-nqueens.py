#!/usr/bin/python3
import sys


def is_safe(board, row, col, n):
    """
    Check if a queen can be placed on board[row][col]
    """
    for i in range(col):
        if board[i] == row or \
           board[i] - i == row - col or \
           board[i] + i == row + col:
            return False
    return True


def solve(board, col, n):
    """
    Solve the N queens problem and print the solutions
    """
    if col == n:
        print_solution(board, n)
        return

    for row in range(n):
        if is_safe(board, row, col, n):
            board[col] = row
            solve(board, col + 1, n)


def print_solution(board, n):
    """
    Print a single solution in the specified format
    """
    solution = [[i, board[i]] for i in range(n)]
    print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solve(board, 0, n)
