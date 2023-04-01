n, m = map(int, input().split())
series = list(map(int, input().split()))
series = list(set(series))
series.sort()

result = []
def f():
  if len(result) == m:
    print(*result)
    return
  
  for i in range(len(series)):
    if result and series[i] < result[-1]: continue

    result.append(series[i])
    f()
    result.pop()

f()