import sys
input = sys.stdin.readline

N = int(input())

nums = []
dic = {}
for _ in range(N):
  num = int(input())
  nums.append(num)

  if num in dic:
    dic[num] += 1
  else:
    dic[num] = 1

nums.sort()
dic = sorted(dic.items(), key=lambda x: (x[1], -x[0]))

print(round(sum(nums) / N))
print(nums[N // 2])
if N == 1:
  print(nums[0])
else:
  if dic[-1][1] == dic[-2][1]:
    print(dic[-2][0])
  else:
    print(dic[-1][0])
print(nums[N - 1] - nums[0])