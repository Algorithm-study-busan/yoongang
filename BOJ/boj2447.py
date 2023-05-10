def f(r, c, length):
  if length == 3:
    for i in range(3):
      result[r][c + i] = '*'
      result[r + 2][c + i] = '*'
      if i != 1:
        result[r + 1][c + i] = '*'
    return
  
  nl = length // 3
  f(r, c, nl)
  f(r, c + nl, nl)
  f(r, c + nl * 2, nl)
  f(r + nl, c, nl)
  f(r + nl, c + nl * 2, nl)
  f(r + nl * 2, c, nl)
  f(r + nl * 2, c + nl, nl)
  f(r + nl * 2, c + nl * 2, nl)

n = int(input())

result = [[' '] * n for _ in range(n)]
f(0, 0, n)

for i in result:
  print(''.join(i))