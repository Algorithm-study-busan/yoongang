def get_sum(length):
  result = 0
  for height in tree:
    if height > length:
      result += height - length
  return result

n, m = map(int, input().split())
tree = list(map(int, input().split()))

M = max(tree)
start = 0
end = M

result = 0
while start <= end:
  mid = (start + end) // 2
  if get_sum(mid) >= m:
    result = result if result > mid else mid
    start = mid + 1
  elif get_sum(mid) < m:
    end = mid - 1

print(result)
