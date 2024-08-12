n, k = map(int, input().split())

items = []
for _ in range(n):
  items.append(list(map(int, input().split())))

dp = [[0] * (k + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
  now_w, now_v = items[i - 1]

  # 현재 넣을 수 있는 최대 무게(j)가 현재 물건의 무게보다 작으면
  for j in range(1, k + 1):
    # 이전 물건에서 선택한 최대 무게를 가져오고
    if now_w > j:
      dp[i][j] = dp[i - 1][j]
    # 아니라면 최대 무게(j)로 담을 수 있는 최대 무게를 다시 측정한다.
    else:
      dp[i][j] = max(now_v + dp[i - 1][j - now_w], dp[i - 1][j])

print(dp[n][k])
