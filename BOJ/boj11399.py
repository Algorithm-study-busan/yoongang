n = int(input())
nums = list(map(int, input().split(' ')))

nums.sort()
result = 0
for i in range(n):
  result += nums[i] * (n - i)

print(result)
