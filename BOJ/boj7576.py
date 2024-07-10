from collections import deque

m, n = map(int, input().split())

tomato = []
for _ in range(n):
  tomato.append(list(map(int, input().split())))

q = deque()
for i in range(n):
  for j in range(m):
    if tomato[i][j] == 1:
      q.append((i, j))

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

while q:
  now_r, now_c = q.popleft()
  
  for i in range(4):
    if now_r + dr[i] >= 0 and now_r + dr[i] < n and now_c + dc[i] >= 0 and now_c + dc[i] < m:
      next_r = now_r + dr[i]
      next_c = now_c + dc[i]
      
      if tomato[next_r][next_c] == 0:
        q.append((next_r, next_c))
        tomato[next_r][next_c] = tomato[now_r][now_c] + 1

result = 0
for i in range(n):
  if result == -1: break

  for j in range(m):
    if tomato[i][j] == 0:
      result = -1
      break

    if tomato[i][j] > result:
      result = tomato[i][j]

if result == 1:
  print(0)
elif result == -1:
  print(result)
else:
  print(result - 1)
