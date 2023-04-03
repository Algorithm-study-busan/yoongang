def get_dist(r1, c1, r2, c2):
  return abs(r1 - r2) + abs(c1 - c2)

def solution():
  result1 = []
  for h in house:
    count = []

    for s in store:
      count.append(get_dist(h[0], h[1], s[0], s[1]))

    result1.append(min(count))
  result2.append(sum(result1))

def f(idx):
  if len(store) == m:
    solution()
    return

  for i in range(idx, len(chicken)):
    store.append(chicken[i])
    f(i + 1)
    store.pop()

n, m = map(int, input().split())
city = []
for _ in range(n):
  city.append(list(map(int, input().split())))

chicken = []
house = []
for i in range(n):
  for j in range(n):
    if city[i][j] == 2:
      chicken.append((i, j))
    elif city[i][j] == 1:
      house.append((i, j))

store = []
result2 = []
f(0)
print(min(result2))