n, m = map(int, input().split())
items = {}
itemList = []
for i in range(n):
  item = input()
  items[item] = i + 1
  itemList.append(item)

for _ in range(m):
  command = input()

  if command.isalpha():
    print(items[command])
  else:
    print(itemList[int(command) - 1])
