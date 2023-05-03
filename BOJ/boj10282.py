import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist: continue

    for next_node, d in graph[now]:
      cost = dist + d
      if cost < distance[next_node]:
        distance[next_node] = cost
        heapq.heappush(q, (cost, next_node))

t = int(input())

for _ in range(t):
  n, d, c = map(int, input().split())

  graph = [[] for _ in range(n + 1)]
  for _ in range(d):
    a, b, s = map(int, input().split())
    graph[b].append((a, s))

  distance = [INF] * (n + 1)
  dijkstra(c)

  count = 0
  m = 0
  for i in distance:
    if i != INF:
      count += 1
      m = max(m, i)
  print(count, end=' ')
  print(m)
