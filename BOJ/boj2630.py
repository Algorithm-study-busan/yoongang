n = int(input())

paper = []
for _ in range(n):
  paper.append(list(map(int, input().split())))

result = [0, 0]

def check_all(paper, r, c, l):
  type = paper[r][c]
  for i in range(r, r + l):
    for j in range(c, c + l):
      if paper[i][j] != type:
        return 0
  return 1

def solution(paper, r, c, l):
  if l == 1 or check_all(paper, r, c, l):
    if paper[r][c] == 1:
      result[1] += 1
    else:
      result[0] += 1
    return
  
  solution(paper, r, c, l // 2)
  solution(paper, r + l // 2, c, l // 2)
  solution(paper, r, c + l // 2, l // 2)
  solution(paper, r + l // 2, c + l // 2, l // 2)

solution(paper, 0, 0, n)
print(result[0])
print(result[1])
