from collections import deque

def bfs():
  q = deque()
  q.append((0, 0))
  visited = [[False] * m for _ in range(n)]
  visited[0][0] = True

  while q:
    now_r, now_c = q.popleft()

    for i in range(4):
      if now_r + dr[i] >= 0 and now_r + dr[i] < n and now_c + dc[i] >= 0 and now_c + dc[i] < m:
        next_r = now_r + dr[i]
        next_c = now_c + dc[i]

        # 공기 부분을 탐색하면서 공기 주변에 치즈가 있으면 카운트
        if not visited[next_r][next_c] and cheese[next_r][next_c] == 0:
          q.append((next_r, next_c))
          visited[next_r][next_c] = True

        if cheese[next_r][next_c] > 0:
          cheese[next_r][next_c] += 1

def check():
  for i in range(n):
    for j in range(m):
      if cheese[i][j] == 0: continue

      if cheese[i][j] >= 3:
        cheese[i][j] = 0
      else:
        cheese[i][j] = 1
  
  for i in range(n):
    for j in range(m):
      if cheese[i][j] == 1:
        return 1
  
  return 0

n, m = map(int, input().split())

cheese = []
for _ in range(n):
  cheese.append(list(map(int, input().split())))

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

count = 0
while check():
  bfs()
  count += 1

print(count)
