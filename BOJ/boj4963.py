from collections import deque

def bfs(r, c):
  q = deque()
  q.append((r, c))
  board[r][c] = 0

  while q:
    now_r, now_c = q.popleft()

    for i in range(8):
      if now_r + dr[i] < h and now_c + dc[i] < w and now_r + dr[i] >= 0 and now_c + dc[i] >= 0:
        nr = now_r + dr[i]
        nc = now_c + dc[i]

        if board[nr][nc] == 1:
          q.append((nr, nc))
          board[nr][nc] = 0

dr = [0, 1, 1, 1, 0, -1, -1, -1]
dc = [1, 1, 0, -1, -1, -1, 0, 1]

while True:
  w, h = map(int, input().split())
  if w == 0 and h == 0:
    break

  board = []
  for _ in range(h):
    board.append(list(map(int, input().split())))

  count = 0
  for i in range(h):
    for j in range(w):
      if board[i][j] == 1:
        count += 1
        bfs(i, j)
  
  print(count)