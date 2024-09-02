import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find_parent(parents, x):
  if parents[x] != x:
    parents[x] =  find_parent(parents, parents[x])
  return parents[x]

def union(parents, x, y):
  a = find_parent(parents, x)
  b = find_parent(parents, y)

  if a < b:
    parents[b] = a
  else:
    parents[a] = b

v, e = map(int, input().split())

edges = []
for _ in range(e):
  a, b, c = map(int, input().split())
  edges.append((c, a, b))

# 비용 기준으로 정렬(오름차순)
edges.sort()

parents = [i for i in range(v + 1)]

result = 0
for edge in edges:
  cost, a, b = edge
  # 사이클을 생성하지 않으면 최소 스패닝 트리에 추가
  if find_parent(parents, a) != find_parent(parents, b):
    union(parents, a, b)
    result += cost

print(result)
