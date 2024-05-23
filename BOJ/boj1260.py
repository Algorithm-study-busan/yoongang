from collections import deque

def bfs(start):
  q = deque()
  q.append(start)
  visited[start] = True

  while q:
    now = q.popleft()
    print(now, end=' ')
    for next in graph[now]:
      if not visited[next]:
        q.append(next)
        visited[next] = True

def dfs(start):
  print(start, end=' ')
  visited[start] = True

  for next in graph[start]:
    if not visited[next]:
      dfs(next)

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
  s, e = map(int, input().split())
  graph[s].append(e)
  graph[e].append(s)

for vect in graph:
  vect.sort()

visited = [False] * (n + 1)
dfs(v)
print()
visited = [False] * (n + 1)
bfs(v)
