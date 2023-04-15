def delete(idx):
  graph[idx] = -2

  for i in range(n):
    if graph[i] == idx:
      delete(i)

n = int(input())
graph = list(map(int, input().split()))
m = int(input())

delete(m)

result = 0
for i in range(n):
  if graph[i] != -2:
    if i not in graph:
      result += 1

print(result)