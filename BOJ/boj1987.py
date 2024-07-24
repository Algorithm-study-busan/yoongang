import sys

input = sys.stdin.readline

def dfs(nr, nc, cnt):
  global result
  result = max(result, cnt)
  
  for i in range(4):
    if nr + dr[i] >= 0 and nr + dr[i] < r and nc + dc[i] >= 0 and nc + dc[i] < c:
      next_r = nr + dr[i]
      next_c = nc + dc[i]
      if not alphabet[ord(board[next_r][next_c]) - 65]:
        alphabet[ord(board[next_r][next_c]) - 65] = True
        dfs(next_r, next_c, cnt + 1)
        alphabet[ord(board[next_r][next_c]) - 65] = False

r, c = map(int, input().split())

board = []
for _ in range(r):
  board.append(list(input()))

alphabet = [False] * 26
alphabet[ord(board[0][0]) - 65] = True

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

result = 0
dfs(0, 0, 1)

print(result)
