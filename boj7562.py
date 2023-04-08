from collections import deque

INF = int(1e9)

def bfs(r, c):
  q = deque()
  q.append((r, c))
  board[r][c] = 1

  while q:
    now_r, now_c = q.popleft()

    for i in range(8):
      if now_r + dr[i] < l and now_c + dc[i] < l and now_r + dr[i] >= 0 and now_c + dc[i] >= 0:
        nr = now_r + dr[i]
        nc = now_c + dc[i]

        if board[nr][nc] == 0:
          q.append((nr, nc))
          board[nr][nc] = board[now_r][now_c] + 1

        if board[nr][nc] == INF:
          print(board[now_r][now_c])
          return

dr = [1, 2, 2, 1, -1, -2, -2, -1]
dc = [2, 1, -1, -2, -2, -1, 1, 2]

t = int(input())

for _ in range(t):
  l = int(input())
  board = [[0] * l for _ in range(l)]

  sr, sc = map(int, input().split())
  rr, rc = map(int, input().split())
  if sr == rr and sc == rc:
    print(0)
    continue
  
  board[rr][rc] = INF

  bfs(sr, sc)