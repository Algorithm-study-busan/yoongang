def binary_search(nums, target):
  start = 0
  end = len(nums) - 1

  while start <= end:
    mid = (start + end) // 2
    if nums[mid] == target:
      return mid
    elif nums[mid] > target:
      end = mid - 1
    else:
      start = mid + 1

n = int(input())
points = list(map(int, input().split()))

sorted_points = sorted(list(set(points)))

print(*list(map(lambda x: binary_search(sorted_points, x), points)))
