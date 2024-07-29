import sys
import heapq

input = sys.stdin.readline
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

n, e = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(e):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))

u, v = map(int, input().split())

points = [(1, u), (1, v), (u, v), (u, n), (v, n)]
dists = []
for i in range(5):
  distance = [INF] * (n + 1)
  dijkstra(points[i][0], distance)
  dists.append(distance[points[i][1]])

if INF in dists:
  print(-1)
else:
  print(min(dists[0] + dists[2] + dists[4], dists[1] + dists[2] + dists[3]))
