import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
      continue

    for next_node, d in graph[now]:
      cost = dist + d

      if distance[next_node] > cost:
        distance[next_node] = cost
        course[next_node] = now
        heapq.heappush(q, (cost, next_node))

def find_course(n):
  if course[n] == 0:
    result.append(n)
    return
  
  result.append(n)
  find_course(course[n])

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
s, e = map(int, input().split())

distance = [INF] * (n + 1)
course = [0] * (n + 1)

dijkstra(s)

result = []
find_course(e)

print(distance[e])
print(len(result))
print(*result[::-1])