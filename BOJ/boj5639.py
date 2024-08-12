import sys
sys.setrecursionlimit(1000000)

def postorder(start, end):
  if start > end: return

  # nums[i] > nums[start] 조건을 만족하는 i가 없는 경우 모두 왼쪽 자식 노드
  mid = end + 1
  # start 노드보다 큰 노드들은 오른쪽 자식
  for i in range(start + 1, end + 1):
    if nums[i] > nums[start]:
      mid = i
      break
  
  # print(nums[start]) 전위순회
  postorder(start + 1, mid - 1)
  postorder(mid, end)
  print(nums[start])

nums = []

while True:
  try:
    nums.append(int(input()))
  except:
    break

postorder(0, len(nums) - 1)