from collections import deque

n, m = map(int, input().split())

q = deque()
visited = [[False] * m for _ in range(n)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

ground = []
for i in range(n):
  ground.append(list(map(int, input().split())))

tmp = 0
for i in range(n):
  if tmp: break

  for j in range(m):
    if ground[i][j] == 2:
      ground[i][j] = 0
      tmp = 1
      q.append((i, j))
      visited[i][j] = True
      break

while q:
  now_r, now_c = q.popleft()

  for i in range(4):
    if now_r + dr[i] >= 0 and now_r + dr[i] < n and now_c + dc[i] >= 0 and now_c + dc[i] < m:
      next_r = now_r + dr[i]
      next_c = now_c + dc[i]
      if ground[next_r][next_c] == 1 and not visited[next_r][next_c]:
        q.append((next_r, next_c))
        visited[next_r][next_c] = True
        ground[next_r][next_c] = ground[now_r][now_c] + 1

for i in range(n):
  for j in range(m):
    # 원래 갈 수 있는 땅인 부분 중에서 도달할 수 없는 위치는 -1을 출력
    if ground[i][j] == 1 and not visited[i][j]:
      print(-1, end=' ')
    else:
      print(ground[i][j], end=' ')
  print()
