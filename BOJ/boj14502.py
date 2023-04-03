from collections import deque
import copy
import sys
input = sys.stdin.readline

result = 0

def bfs(r, c, b):
  q = deque()
  q.append((r, c))

  while q:
    now_r, now_c = q.popleft()

    for i in range(4):
      if now_r + dr[i] < n and now_c + dc[i] < m and now_r + dr[i] >= 0 and now_c + dc[i] >= 0:
        nr = now_r + dr[i]
        nc = now_c + dc[i]
        if b[nr][nc] == 0:
          b[nr][nc] = 2
          q.append((nr, nc))

def solution():
  global result
  result_board = copy.deepcopy(board)
  
  for v in virus:
    bfs(v[0], v[1], result_board)
  
  count = 0
  for i in range(n):
    for j in range(m):
      if result_board[i][j] == 0:
        count += 1
  
  result = max(result, count)


def wall(count):
  global result
  if count == 3:
    solution()
    return
  
  for i in range(n):
    for j in range(m):
      if board[i][j] == 0:
        board[i][j] = 1
        wall(count + 1)
        board[i][j] = 0

n, m = map(int, input().split())
board = []
for _ in range(n):
  board.append(list(map(int, input().split())))

virus = []
for i in range(n):
  for j in range(m):
    if board[i][j] == 2:
      virus.append((i, j))

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

wall(0)

print(result)