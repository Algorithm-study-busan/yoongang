import sys
from collections import deque

input = sys.stdin.readline

def topologry_sort():
  q = deque()

  for i in range(1, n + 1):
    if indegrees[i] == 0:
      q.append(i)
      dp[i] = costs[i]
  
  while q:
    now = q.popleft()

    if now == w: return

    for next in orders[now]:
      indegrees[next] -= 1
      dp[next] = max(dp[next], dp[now] + costs[next])

      if indegrees[next] == 0:
        q.append(next)

t = int(input())

for _ in range(t):
  n, k = map(int, input().split())

  costs = [0] + list(map(int, input().split()))
  orders = [[] for _ in range(n + 1)]
  indegrees = [0] * (n + 1)
  dp = [0] * (n + 1)
  for _ in range(k):
    x, y = map(int, input().split())
    orders[x].append(y)
    indegrees[y] += 1

  w = int(input())

  topologry_sort()

  print(dp[w])
