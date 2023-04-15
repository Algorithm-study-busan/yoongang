from collections import deque

INF = int(1e9)

def bfs():
  q = deque()
  q.append((0, 0))
  distance[0][0] = board[0][0]

  while q:
    r, c = q.popleft()

    for i in range(4):
      nr = r + dr[i]
      nc = c + dc[i]
      if nr < n and nc < n and nr >= 0 and nc >= 0:
        if distance[r][c] + board[nr][nc] < distance[nr][nc]:
          distance[nr][nc] = distance[r][c] + board[nr][nc]
          q.append((nr, nc))

problem = 1
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

while True:
  n = int(input())

  if n == 0:
    break

  board = []
  for _ in range(n):
    board.append(list(map(int, input().split())))
  distance = [[INF] * n for _ in range(n)]

  bfs()
  print(f'Problem {problem}: {distance[n - 1][n - 1]}')
  problem += 1