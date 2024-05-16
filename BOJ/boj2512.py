def get_sum(value):
  result = 0
  for price in prices:
    result += price if value >= price else value
  return result

n = int(input())
prices = list(map(int, input().split()))
prices.sort()
total = int(input())

if sum(prices) <= total:
  print(prices[-1])
else:
  start = 1
  end = prices[-1]

  result = 1
  while start <= end:
    mid = (start + end) // 2
    val = get_sum(mid)

    if val < total:
      start = mid + 1
      if result < mid:
        result = mid
    elif val > total:
      end = mid - 1
    else:
      result = mid
      break

  print(result)
