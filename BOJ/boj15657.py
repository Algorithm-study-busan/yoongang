n, m = map(int, input().split())

series = list(map(int, input().split()))
series.sort()

result = []
def f(start):
  if len(result) == m:
    print(' '.join(map(str, result)))
    return
  
  for i in range(start, len(series)):
    result.append(series[i])
    f(i)
    result.pop()

f(0)