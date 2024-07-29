n = int(input())

prices = []
for _ in range(n):
  prices.append(list(map(int, input().split())))

dp = [[0] * 3 for _ in range(n)]
dp[0] = prices[0]

for i in range(1, n):
  for j in range(3):
    dp[i][j] = prices[i][j] + min(dp[i - 1][(j + 1) % 3], dp[i - 1][(j + 2) % 3])

print(min(dp[n - 1]))
