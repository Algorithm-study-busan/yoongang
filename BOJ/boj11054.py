n = int(input())
nums = list(map(int, input().split()))
reverse_nums = nums[::-1]

dp_increase = [1] * n
dp_decrease = [1] * n

for i in range(n):
  for j in range(i):
    if nums[j] < nums[i]:
      dp_increase[i] = max(dp_increase[i], dp_increase[j] + 1)
    if reverse_nums[j] < reverse_nums[i]:
      dp_decrease[i] = max(dp_decrease[i], dp_decrease[j] + 1)

result = [1] * n
for i in range(n):
  result[i] = dp_increase[i] + dp_decrease[n - i - 1] - 1

print(max(result))