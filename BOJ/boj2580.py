import sys
input = sys.stdin.readline

def check_row(r, n):
  for i in range(9):
    if n == board[r][i]:
      return False
  return True

def check_column(c, n):
  for i in range(9):
    if n == board[i][c]:
      return False
  return True

def check_box(r, c, n):
  r_start, c_start = r // 3 * 3, c // 3 * 3
  for i in range(r_start, r_start + 3):
    for j in range(c_start, c_start + 3):
      if n == board[i][j]:
        return False
  return True

def f(idx):
  if idx == len(change_list):
    for row in board:
      print(*row)
    exit(0)

  for i in range(1, 10):
    r, c = change_list[idx]

    if check_row(r, i) and check_column(c, i) and check_box(r, c, i):
      board[r][c] = i
      f(idx + 1)
      board[r][c] = 0

board = []
for _ in range(9):
  board.append(list(map(int, input().split())))

change_list = []
for i in range(9):
  for j in range(9):
    if board[i][j] == 0:
      change_list.append((i, j))

f(0)