from collections import deque

def bfs():
  q = deque()
  q.append((0, 0))
  count[0][0] = 0

  while q:
    r, c = q.popleft()

    for i in range(4):
      nr = r + dr[i]
      nc = c + dc[i]
      if nr < n and nc < m and nr >= 0 and nc >= 0:
        if count[nr][nc] == -1:
          if board[nr][nc] == 0:
            # 벽이 아닌 길을 먼저 탐색하기 위해 appendleft를 사용한다.
            q.appendleft((nr, nc))
            count[nr][nc] = count[r][c]
          else:
            q.append((nr, nc))
            count[nr][nc] = count[r][c] + 1

m, n = map(int, input().split())
board = []
for _ in range(n):
  lst = list(input())
  board.append(list(map(int, lst)))

count = [[-1] * m for _ in range(n)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

bfs()
print(count[n - 1][m - 1])