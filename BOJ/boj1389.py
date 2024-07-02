INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
  for j in range(1, n + 1):
    if i == j: graph[i][j] = 0

for _ in range(m):
  a, b = map(int, input().split())

  graph[a][b] = 1
  graph[b][a] = 1

for k in range(1, n + 1):
  for i in range(1, n + 1):
    for j in range(1, n + 1):
      graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

res = [101, INF]
for i in range(1, n + 1):
  tmp = 0
  for j in range(1, n + 1):
    tmp += graph[i][j]
  
  if tmp < res[1]:
    res = [i, tmp]

print(res[0])
