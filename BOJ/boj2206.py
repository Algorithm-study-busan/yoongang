from collections import deque

def bfs(r, c, b):
  q = deque()
  q.append((r, c, b))
  distance[r][c][b] = 1

  while q:
    now_r, now_c, now_b = q.popleft()

    if now_r == n - 1 and now_c == m - 1:
      return distance[now_r][now_c][now_b]
    
    for i in range(4):
      if now_r + dr[i] >= 0 and now_r + dr[i] < n and now_c + dc[i] >= 0 and now_c + dc[i] < m:
        nr = now_r + dr[i]
        nc = now_c + dc[i]
        if board[nr][nc] == '1' and now_b == 0:
          distance[nr][nc][1] = distance[now_r][now_c][0] + 1
          q.append((nr, nc, 1))
        elif board[nr][nc] == '0' and distance[nr][nc][now_b] == 0:
          distance[nr][nc][now_b] = distance[now_r][now_c][now_b] + 1
          q.append((nr, nc, now_b))

  return -1

n, m = map(int, input().split())

board = []
for _ in range(n):
  board.append(list(input()))

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

distance = [[[0, 0] for _ in range(m)] for _ in range(n)]
print(bfs(0, 0, 0))
