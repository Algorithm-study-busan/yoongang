from collections import deque

def topology_sort():
  q = deque()
  result = []

  for i in range(1, n + 1):
    if indegree[i] == 0:
      q.append(i)

  while q:
    now = q.popleft()
    result.append(now)

    for next in comps[now]:
      indegree[next] -= 1

      if indegree[next] == 0:
        q.append(next)
  
  for res in result:
    print(res, end=' ')

n, m = map(int, input().split())

indegree = [0] * (n + 1)

comps = [[] for _ in range(n + 1)]
for _ in range(m):
  a, b = map(int, input().split())
  comps[a].append(b)
  indegree[b] += 1

topology_sort()
