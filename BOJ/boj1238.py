import heapq

def dijkstra(start, distance, graph):
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

INF = int(1e9)

n, m, x = map(int, input().split())

# x에서 다른 모든 노드로 가는 거리를 구하기 위한 그래프
graph = [[] for _ in range(n + 1)]
# 다른 모든 노드에서 x로 가는 거리를 구하기 위한 그래프
reverse_graph = [[] for _ in range(n + 1)]
for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  reverse_graph[b].append((a, c))

distance = [INF] * (n + 1)
dijkstra(x, distance, graph)
reverse_distance = [INF] * (n + 1)
dijkstra(x, reverse_distance, reverse_graph)

result = 0
for i in range(1, n + 1):
  if i == x: continue

  if result < distance[i] + reverse_distance[i]:
    result = distance[i] + reverse_distance[i]

print(result)
