p = 1_000_000_007

def fibo(n):
  if dp.get(n) != None:
    return dp[n]
  
  if n % 2 != 0:
    dp[n // 2] = fibo(n // 2) % p
    dp[n // 2 + 1] = fibo(n // 2 + 1) % p

    return dp[n // 2] ** 2 + dp[n // 2 + 1] ** 2
  else:
    dp[n // 2 - 1] = fibo(n // 2 - 1) % p
    dp[n // 2 + 1] = fibo(n // 2 + 1) % p

    return dp[n // 2 + 1] ** 2 - dp[n // 2 - 1] ** 2

n = int(input())
dp = {0: 0, 1: 1, 2: 1}

print(fibo(n) % p)