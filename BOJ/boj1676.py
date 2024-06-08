def factorial(n):
  result = 1
  while n != 0:
    result *= n
    n -= 1
  return result

n = factorial(int(input()))

answer = 0
while n != 0:
  if n % 10 != 0:
    break

  answer += 1
  n //= 10

print(answer)