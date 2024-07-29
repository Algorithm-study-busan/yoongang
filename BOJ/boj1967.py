import heapq

INF = int(1e9)

def dijkstra(start, distance):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist: continue

    for next, d in graph[now]:
      cost = dist + d
      if cost < distance[next]:
        distance[next] = cost
        heapq.heappush(q, (cost, next))

n = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))

distance1 = [INF] * (n + 1)
dijkstra(1, distance1)
idx = distance1.index(max(distance1[1:]))

distance2 = [INF] * (n + 1)
dijkstra(idx, distance2)
print(max(distance2[1:]))
