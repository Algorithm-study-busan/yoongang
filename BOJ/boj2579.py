n = int(input())

stairs = [0] * 300
for i in range(n):
  stairs[i] = int(input())

# index 에러를 방지하기 위해 범위 전체의 리스트를 생성
dp = [0] * 300
dp[0] = stairs[0]
dp[1] = stairs[0] + stairs[1]
dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

# i번째 계단에 오르는 방법은 -3, -1번째를 지나오거나 -2번째를 지나오는 방법 뿐이다.
for i in range(3, n):
  dp[i] = max(dp[i - 3] + stairs[i - 1] + stairs[i], dp[i - 2] + stairs[i])

print(dp[n - 1])
