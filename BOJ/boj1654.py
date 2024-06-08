import sys
sys.setrecursionlimit(10 ** 6)

def count(num):
  result = 0
  for e in lines:
    result += e // num
  return result

def solution(start, end):
  if end < start: return end

  num = (start + end) // 2

  if count(num) >= n:
    return solution(num + 1, end)
  else:
    return solution(start, num - 1)

k, n = map(int, input().split(' '))

lines = []
for _ in range(k):
  lines.append(int(input()))

print(solution(1, max(lines)))
