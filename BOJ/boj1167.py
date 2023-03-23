import sys
input = sys.stdin.readline

def dfs(start):
  for next_node, d in graph[start]:
    if distance[next_node] == -1:
      distance[next_node] = distance[start] + d
      dfs(next_node)

v = int(input())
graph = [[] for _ in range(v + 1)]
for _ in range(v):
  lst = list(map(int, input().split()))
  lst.pop()

  for i in range(1, len(lst), 2):
    graph[lst[0]].append((lst[i], lst[i + 1]))
    graph[lst[i]].append((lst[0], lst[i + 1]))

for i in range(1, v + 1):
  graph[i] = list(set(graph[i]))

distance = [-1] * (v + 1)
distance[1] = 0
dfs(1)
n1 = distance.index(max(distance))

distance = [-1] * (v + 1)
distance[n1] = 0
dfs(n1)
print(max(distance))