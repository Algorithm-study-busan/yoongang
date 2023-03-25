import sys
sys.setrecursionlimit(1000000)

def postorder(start, end):
  if start > end:
    return
  
  target = end + 1
  for i in range(start + 1, end + 1):
    if nums[start] < nums[i]:
      target = i
      break

  postorder(start + 1, target - 1)
  postorder(target, end)
  print(nums[start])

nums = []

while True:
  try:
    nums.append(int(input()))
  except:
    break

postorder(0, len(nums) - 1)