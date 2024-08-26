def count_lect(value):
  total = 0
  count = 1
  for length in lengths:
    if total + length > value:
      total = 0
      count += 1
    total += length

  return count

n, m = map(int, input().split())
lengths = list(map(int, input().split()))

# 블루레이에 적어도 하나의 강의가 들어가야하기 때문에 start의 값은 가장 긴 강의의 길이이다.
start = max(lengths)
end = sum(lengths)
while start <= end:
  mid = (start + end) // 2

  if count_lect(mid) <= m:
    end = mid - 1
  else:
    start = mid + 1

print(start)
