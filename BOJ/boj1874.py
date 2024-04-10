N = int(input())

num = 1
stack = []
result = []
for _ in range(N):
  n = int(input())

  while num <= n:
    stack.append(num)
    num += 1
    result.append('+')

  if stack[-1] == n:
    stack.pop()
    result.append('-')

if len(stack) == 0:
  for i in range(len(result)):
    print(result[i])
else:
  print('NO')