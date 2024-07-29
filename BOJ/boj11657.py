INF = int(1e9)

def bellman_ford():
  distance[1] = 0

  for i in range(n):
    for start, end, dist in edges:
      if distance[start] != INF and distance[end] > distance[start] + dist:
        distance[end] = distance[start] + dist

        if i == n - 1:
          return False
  
  return True

n, m = map(int, input().split())

edges = []
for _ in range(m):
  a, b, c = map(int, input().split())
  edges.append((a, b, c))

distance = [INF] * (n + 1)
result = bellman_ford()

if not result:
  print(-1)
else:
  for i in range(2, n + 1):
    if distance[i] == INF:
      print(-1)
    else:
      print(distance[i])
