n, m = map(int, input().split())

stack = []

def solution(start):
  if len(stack) == m:
    print(*stack)
    return
  
  for i in range(start, n + 1):
    if i not in stack:
      stack.append(i)
      solution(i + 1)
      stack.pop()

solution(1)
