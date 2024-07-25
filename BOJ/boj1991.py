n = int(input())

graph = {}
for _ in range(n):
  a, b, c = input().split()
  graph[a] = (b, c)

def preorder(node):
  print(node, end='')
  left, right = graph[node]

  if left != '.':
    preorder(left)
  if right != '.':
    preorder(right)

def inorder(node):
  left, right = graph[node]
  
  if left != '.':
    inorder(left)
  print(node, end='')
  if right != '.':
    inorder(right)

def postorder(node):
  left, right = graph[node]
  
  if left != '.':
    postorder(left)
  if right != '.':
    postorder(right)
  print(node, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')
