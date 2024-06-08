import sys

input = sys.stdin.readline

N = int(input())

stack = []
length = 0
for _ in range(N):
  type = list(map(int, input().split(' ')))
  command = type[0]
  if command == 1:
    stack.append(type[1])
    length += 1
  elif command == 2:
    if length == 0: print(-1)
    else:
      print(stack.pop())
      length -= 1
  elif command == 3:
    print(length)
  elif command == 4:
    print(1 if length == 0 else 0)
  elif command == 5:
    print(-1 if length == 0 else stack[-1])
    