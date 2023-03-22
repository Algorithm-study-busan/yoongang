import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def dfs(start):
  for next_node, d in graph[start]:
    if distance[next_node] == -1:
      distance[next_node] = distance[start] + d
      dfs(next_node)

n = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))

distance = [-1] * (n + 1)
distance[1] = 0
dfs(1)
n1 = distance.index(max(distance))

distance = [-1] * (n + 1)
distance[n1] = 0
dfs(n1)
print(max(distance))