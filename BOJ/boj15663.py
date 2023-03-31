n, m = map(int, input().split())
series = list(map(int, input().split()))
series.sort()

visited = [False] * n
result = []
def f():
  if len(result) == m:
    print(*result)
    return
  
  prev = 0
  for i in range(n):
    if not visited[i] and prev != series[i]:
      prev = series[i]
      result.append(series[i])
      visited[i] = True
      f()
      result.pop()
      visited[i] = False

f()