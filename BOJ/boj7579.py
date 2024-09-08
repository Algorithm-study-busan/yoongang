n, m = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))

c = sum(cost)
dp = [[0] * (c + 1) for _ in range(n + 1)]

result = int(1e9)
for i in range(1, n + 1):
  now_memory = memory[i - 1]
  now_cost = cost[i - 1]

  # 비용이 0인 경우를 계산하기 위해 0 ~ c 범위
  for j in range(c + 1):
    if now_cost > j:
      dp[i][j] = dp[i - 1][j]
    else:
      dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - now_cost] + now_memory)
    
    # 최소 비용을 위한 메모리가 m 이상인 경우 적용(정확히 m일 필요 x)
    if dp[i][j] >= m:
      result = min(result, j)

print(result)
