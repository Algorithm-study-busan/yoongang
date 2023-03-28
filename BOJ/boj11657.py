import sys
input = sys.stdin.readline
INF = int(1e9)

def bf():
  distance[1] = 0

  for i in range(n):
    for j in range(m):
      now, next, cost = graph[j]

      if distance[now] != INF and distance[next] > distance[now] + cost:
        distance[next] = distance[now] + cost

        if i == n - 1:
          return True
        
  return False

n, m = map(int, input().split())

graph = []
for _ in range(m):
  a, b, c = map(int, input().split())
  graph.append((a, b, c))

distance = [INF] * (n + 1)

negative_cycle = bf()

if negative_cycle:
  print(-1)
else:
  for i in range(2, n + 1):
    if distance[i] == INF:
      print(-1)
    else:
      print(distance[i])