import sys
from collections import deque

input = sys.stdin.readline

def bfs(graph, visited, n):
  q = deque()
  q.append(n)
  visited[n] = True

  while q:
    now = q.popleft()
    for next in graph[now]:
      if not visited[next]:
        q.append(next)
        visited[next] = True

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
  u, v = map(int, input().split())

  graph[u].append(v)
  graph[v].append(u)

visited = [False] * (n + 1)
cnt = 0
for i in range(1, n + 1):
  if not visited[i]:
    bfs(graph, visited, i)
    cnt += 1

print(cnt)
