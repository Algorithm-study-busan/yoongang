from collections import deque

INF = int(1e9)

def bfs(graph, start, distance):
  q = deque()
  q.append(start)
  distance[start] = 0

  while q:
    now = q.popleft()
    
    for next, dist in graph[now]:
      if distance[next] == INF:
        distance[next] = dist + distance[now]
        q.append(next)
  
  return distance.index(max(distance[1:]))

v = int(input())

graph = [[] for _ in range(v + 1)]
for _ in range(v):
  tmp = list(map(int, input().split()))
  a = tmp[0]
  lst = tmp[1:]
  for i in range(len(lst) // 2):
    graph[a].append((lst[i * 2], lst[(i * 2) + 1]))

# 임의의 정점에서 가장 먼 거리에 있는 노드를 구하고(거리1)
# 그 노드에서 가장 먼 거리에 있는 노드를 구했을때(거리2)
# 두 거리 중 더 큰 거리가 트리의 지름이다.
distance = [INF] * (v + 1)
next = bfs(graph, 1, distance)
distance = [INF] * (v + 1)
result = bfs(graph, next, distance)

print(distance[result])
