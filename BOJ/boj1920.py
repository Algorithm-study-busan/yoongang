def binary_search(start, end, target):
  result = 0
  while end >= start:
    mid = (start + end) // 2

    if target > numbers[mid]:
      start = mid + 1
    elif target < numbers[mid]:
      end = mid - 1
    else:
      result = 1
      break
  
  return result

n = int(input())
numbers = list(map(int, input().split(' ')))
numbers.sort()

m = int(input())
nums = list(map(int, input().split(' ')))

for num in nums:
  print(binary_search(0, n - 1, num))