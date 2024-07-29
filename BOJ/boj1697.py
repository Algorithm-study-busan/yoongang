from collections import deque

n, k = map(int, input().split())

INF = int(1e9)
graph = [INF] * 100_001

def bfs(graph, n, k):
  q = deque()
  q.append(n)
  graph[n] = 0
  
  while q:
    now = q.popleft()
    if now == k:
      return graph[now]
    if now + 1 <= 100_000 and graph[now + 1] == INF:
      graph[now + 1] = graph[now] + 1
      q.append(now + 1)
    if now - 1 >= 0 and graph[now - 1] == INF:
      graph[now - 1] = graph[now] + 1
      q.append(now - 1)
    if now * 2 <= 100_000 and graph[now * 2] == INF:
      graph[now * 2] = graph[now] + 1
      q.append(now * 2)

print(bfs(graph, n, k))