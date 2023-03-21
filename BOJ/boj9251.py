# 주어진 두 수열에서 가장 긴 공통 부분수열의 길이를 출력하는 문제이다.
# 수열의 최대 길이가 1000이므로 반복문으로 모든 경우를 비교하면 시간초과가 뜰것같다.
# 이중 dp를 사용해서 공통 부분수열의 최대 길이를 저장한다.
a = input()
b = input()

dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

for i in range(1, len(a) + 1):
  for j in range(1, len(b) + 1):
    # 각 수열에 마지막으로 추가된 문자가 같으면 최대 길이가 1 늘어난다.
    if a[i - 1] == b[j - 1]:
      dp[i][j] = dp[i - 1][j - 1] + 1
    else:
      dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

print(dp[-1][-1])