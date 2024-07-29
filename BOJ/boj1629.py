a, b, c = map(int, input().split())

# 수학 공식 : (A + B) % C = ((A % C) + (B % C)) % C
def solution(a, b, c):
  if b == 1:
    return a % c
  
  if b % 2 == 0:
    return (solution(a, b // 2, c) ** 2) % c
  else:
    return ((solution(a, b // 2, c) ** 2) * a) % c
  
# pow 내장 함수 사용하면 간단 => pow(base, exp, mod=None)
print(solution(a, b, c))
