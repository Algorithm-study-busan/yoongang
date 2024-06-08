def solution(start, end, depth):
  if start == end:
    tree[depth].append(preorder[start])
    return
  
  mid = (start + end) // 2
  tree[depth].append(preorder[mid])
  solution(start, mid - 1, depth + 1)
  solution(mid + 1, end, depth + 1)

k = int(input())

preorder = list(map(int, input().split(' ')))
tree = [[] for _ in range(k)]

solution(0, len(preorder) - 1, 0)
for t in tree:
  print(*t)
  