from collections import deque

n = int(input())
nums = deque([x + 1 for x in range(n)])

for _ in range(n - 1):
  nums.popleft()
  nums.rotate(-1)

print(nums[0])
