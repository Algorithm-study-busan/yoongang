n = int(input())
dists = list(map(int, input().split(' ')))
prices = list(map(int, input().split(' ')))

temp = prices[0]
result = 0
for i in range(0, n - 1):
  if temp > prices[i]:
    temp = prices[i]
  result += temp * dists[i]

print(result)
