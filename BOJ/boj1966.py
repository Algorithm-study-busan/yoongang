from collections import deque

T = int(input())

for _ in range(T):
  N, idx = map(int, input().split(' '))
  docs = deque(list(map(int, input().split(' '))))

  count = 0
  while True:
    if docs[0] == max(docs):
      docs.popleft()
      count += 1

      if idx == 0: break
    else:
      docs.rotate(-1)
    
    idx = (idx - 1) if idx > 0 else (len(docs) - 1)

  print(count)

