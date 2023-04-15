INF = int(1e9)
n, m, r = map(int, input().split())
items = list(map(int, input().split()))

distance = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
  distance[i][i] = 0

for _ in range(r):
  a, b, c = map(int, input().split())
  distance[a][b] = c
  distance[b][a] = c

for bridge in range(1, n + 1):
  for start in range(1, n + 1):
    for end in range(1, n + 1):
      if distance[start][end] > distance[start][bridge] + distance[bridge][end]:
        distance[start][end] = distance[start][bridge] + distance[bridge][end]

result = 0
for i in range(1, n + 1):
  count = 0
  for j in range(1, n + 1):
    if distance[i][j] <= m:
      count += items[j - 1]
  
  result = max(result, count)

print(result)