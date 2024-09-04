import sys

input = sys.stdin.readline

def find_parent(parents, x):
  if parents[x] != x:
    parents[x] = find_parent(parents, parents[x])
  return parents[x]

def union(parents, x, y):
  a = find_parent(parents, x)
  b = find_parent(parents, y)

  if a < b:
    parents[b] = a
  else:
    parents[a] = b

n, m = map(int, input().split())

result = 0
parents = [i for i in range(n)]
for i in range(m):
  a, b = map(int, input().split())
  if find_parent(parents, a) != find_parent(parents, b):
    union(parents, a, b)
  elif result == 0:
    result = i + 1

print(result)
