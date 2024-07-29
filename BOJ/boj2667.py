from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

n = int(input())

def bfs(ground, visited, r, c):
  q = deque()
  q.append((r, c))
  visited[r][c] = True

  count = 0
  while q:
    count += 1
    now_r, now_c = q.popleft()
    for i in range(4):
      if now_r + dr[i] >= 0 and now_r + dr[i] < n and now_c + dc[i] >= 0 and now_c + dc[i] < n:
        next_r = now_r + dr[i]
        next_c = now_c + dc[i]
        if not visited[next_r][next_c] and ground[next_r][next_c] == 1:
          q.append((next_r, next_c))
          visited[next_r][next_c] = True
  
  return count

ground = []
for _ in range(n):
  ground.append(list(map(int, list(input()))))

result = []
visited = [[False] * n for _ in range(n)]
for i in range(n):
  for j in range(n):
    if ground[i][j] == 1 and not visited[i][j]:
      result.append(bfs(ground, visited, i, j))

print(len(result))
result.sort()
for l in result:
  print(l)
