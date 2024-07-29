import sys

INF = int(1e9)
input = sys.stdin.readline

def bellman_ford(edges, distance, v):
  # 시작점에 제한이 없기 때문에 시작점의 distance를 0으로 해주는 단계를 생략
  for i in range(v):
    for s, e, d in edges:
      # 시작점에 상관없이 negative cycle의 존재 여부만 체크하면 되기 때문에 distance[e] != INF 조건을 생략
      if distance[e] > distance[s] + d:
        distance[e] = distance[s] + d

        if i == v - 1:
          return False
        
  return True

t = int(input())

for _ in range(t):
  n, m, w = map(int, input().split())

  edges = []
  for _ in range(m):
    s, e, t = map(int, input().split())

    edges.append((s, e, t))
    edges.append((e, s, t))
  
  for _ in range(w):
    s, e, t = map(int, input().split())

    edges.append((s, e, -t))

  distance = [INF] * (n + 1)
  if bellman_ford(edges, distance, n):
    print('NO')
  else:
    print('YES')
