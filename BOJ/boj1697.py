from collections import deque

t = int(input())

for _ in range(t):
  p = input()
  n = int(input())
  nums = input()
  nums = nums.replace('[','')
  nums = nums.replace(']','')
  nums = deque(nums.split(','))

  if n == 0 and 'D' in p:
    print('error')
    continue
  
  tmp = 0
  err = False
  for c in p:
    if c == 'R':
      tmp = 0 if tmp == -1 else -1
      continue
    
    if n == 0:
      err = True
      print('error')
      break

    if tmp == 0:
      nums.popleft()
    else:
      nums.pop()
    n -= 1
  
  if err: continue

  if tmp == -1:
    nums.reverse()
  
  print('[' + ','.join(nums) + ']')
