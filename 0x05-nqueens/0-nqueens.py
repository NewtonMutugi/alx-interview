#!/usr/bin/python3
"""
N queens puzzle
"""
import sys


def is_safe(board, row, col, n):
  """
  Check if a queen can be placed on board[row][col]
  """
  for i in range(col):
    if board[row][i] == 1:
      return False

  for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
    if board[i][j] == 1:
      return False

  for i, j in zip(range(row, n, 1), range(col, -1, -1)):
    if board[i][j] == 1:
      return False

  return True


def solve(board, col, n):
  """
  Solve the N queens problem
  """
  if col == n:
    for row in range(n):
      for col in range(n):
        if board[row][col] == 1:
          print("[{}, {}]".format(row, col), end="")
    print()
    return True

  res = False
  for row in range(n):
    if is_safe(board, row, col, n):
      board[row][col] = 1
      res = solve(board, col + 1, n) or res
      board[row][col] = 0

  return res


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

  board = [[0 for j in range(n)] for i in range(n)]
  solve(board, 0, n)
