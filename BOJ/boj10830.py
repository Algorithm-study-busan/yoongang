import sys
input = sys.stdin.readline

def multiply(m1, m2):
  result = [[0] * n for _ in range(n)]

  for i in range(n):
    for j in range(n):
      r = 0
      for h in range(n):
        r += m1[i][h] * m2[h][j]
      result[i][j] = r % 1000

  return result

def f(m, s):
  if s == 1:
    return m
  
  mtx = f(m, s // 2)
  if s % 2 == 0:
    return multiply(mtx, mtx)
  else:
    return multiply(multiply(mtx, mtx), m)
  

n, b = map(int, input().split())

matrix = []
for _ in range(n):
  matrix.append(list(map(int, input().split())))

result = f(matrix, b)
for i in range(n):
  for j in range(n):
    print(result[i][j] % 1000, end=' ')
  print()
