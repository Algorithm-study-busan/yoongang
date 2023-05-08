def f(r, c, w, h):
  if w == 5:
    board[r][c] = '*'
    board[r + 1][c - 1] = '*'
    board[r + 1][c + 1] = '*'
    for i in range(5):
      board[r + 2][c + i - 2] = '*'
    return

  nw = w // 2
  nh = h // 2
  f(r, c, nw, nh)
  f(r + nh, c - nw // 2 - 1, nw, nh)
  f(r + nh, c + nw // 2 + 1, nw, nh)

n = int(input())
m = n // 3
length = 5 * m + m - 1
board = [[' '] * length for _ in range(n)]

f(0, length // 2, length, n)
for i in board:
  print(''.join(i))