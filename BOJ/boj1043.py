# 재귀
# n, m = map(int, input().split())
# people = list(map(int, input().split()))
# people.pop(0)

# party = []
# for _ in range(m):
#   lst = list(map(int, input().split()))
#   lst.pop(0)
#   party.append(lst)

# cnt = 0
# visited = [False] * m

# def solution(person, visited):
#   cnt = 0
#   for i in range(m):
#     if person in party[i] and not visited[i]:
#       visited[i] = True
#       cnt += 1
#       for j in range(len(party[i])):
#         cnt += solution(party[i][j], visited)
#   return cnt

# for p in people:
#   cnt += solution(p, visited)

# print(m - cnt)

# union-find
def find_parent(parents, x):
  if parents[x] != x:
    return find_parent(parents, parents[x])
  return parents[x]

def union(parents, a, b, known):
  a = find_parent(parents, a)
  b = find_parent(parents, b)
  
  # 진실을 아는 사람과 union하면 진실을 아는 사람이 부모가 되도록
  if a in known and b in known: return

  if a in known:
    parents[b] = a
  elif b in known:
    parents[a] = b
  else:
    if a < b:
      parents[b] = a
    else:
      parents[a] = b

n, m = map(int, input().split())
known = list(map(int, input().split()))[1:]

parents = [i for i in range(n + 1)]
parties = []
for _ in range(m):
  lst = list(map(int, input().split()))
  length = lst[0]
  party = lst[1:]
  for i in range(length - 1):
    union(parents, party[i], party[i + 1], known)

  parties.append(party)

result = m
for party in parties:
  for p in party:
    if find_parent(parents, p) in known:
      result -= 1
      break

print(result)
