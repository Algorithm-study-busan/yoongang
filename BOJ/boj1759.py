def check():
  count = 0
  for i in result:
    if i in a:
      count += 1
  
  if count >= 1 and len(result) - count >= 2:
    return True
  else:
    return False

def f(idx):
  if len(result) == l:
    if check():
      print(''.join(result))
      return
  
  for i in range(idx, c):
    result.append(s[i])
    f(i + 1)
    result.pop()

l, c = map(int, input().split())
s = list(input().split())
s.sort()

a = ['a', 'e', 'i', 'o', 'u']
result = []
f(0)