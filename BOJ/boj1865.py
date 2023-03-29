import sys
input = sys.stdin.readline
INF = int(1e9)

def bf():
  for i in range(n):
    for j in range(len(graph)):
      now, next, cost = graph[j]

      if distance[next] > distance[now] + cost:
        distance[next] = distance[now] + cost

        if i == n - 1:
          return True
        
  return False

t = int(input())

for _ in range(t):
  n, m, w = map(int, input().split())

  graph = []
  for _ in range(m):
    s, e, t = map(int, input().split())
    graph.append((s, e, t))
    graph.append((e, s, t))

  for _ in range(w):
    s, e, t = map(int, input().split())
    graph.append((s, e, -t))
  
  distance = [INF] * (n + 1)
  result = bf()
  
  if result:
    print('YES')
  else:
    print('NO')
