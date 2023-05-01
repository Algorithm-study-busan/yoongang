def check(idx):
  for i in range(idx):
    if queen[idx] == queen[i] or abs(queen[idx] - queen[i]) == abs(idx - i):
      return False
  return True

def f(idx):
  global count
  if idx == n:
    count += 1
    return
  
  for i in range(n):
    queen[idx] = i
    
    if check(idx):
      f(idx + 1)

n = int(input())

board = [[0] * n for _ in range(n)]
count = 0
queen = [0] * n

f(0)
print(count)