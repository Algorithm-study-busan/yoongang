n, r, c = map(int, input().split())

def solution(n, r, c, res):
  if n == 0: return res

  if (2 ** n) / 2 <= r:
    res += (((2 ** n) // 2) ** 2) * 2
    r -= (2 ** n) // 2
  
  if (2 ** n) / 2 <= c:
    res += ((2 ** n) // 2) ** 2
    c -= (2 ** n) // 2
  
  return solution(n - 1, r, c, res)

print(solution(n, r, c, 0))
