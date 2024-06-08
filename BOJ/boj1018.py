def solution(board, x_start, y_start, type):
  count1 = 0
  count2 = 0
  start = (x_start + y_start) % 2
  for i in range(x_start, x_start + 8):
    for j in range(y_start, y_start + 8):
      if (start == (i + j) % 2 and board[i][j] != type) or (start != (i + j) % 2 and board[i][j] == type):
        count1 += 1
      if (start == (i + j) % 2 and board[i][j] == type) or (start != (i + j) % 2 and board[i][j] != type):
        count2 += 1
  
  return min(count1, count2)

[n, m] = list(map(int, input().split(' ')))
board = []
for _ in range(n):
  board.append(list(input()))

answer = 65
for i in range(n - 7):
  if answer == 0: break

  for j in range(m - 7):
    result = solution(board, i, j, board[i][j])

    if result == 0:
      answer = 0
      break
    
    if answer > result:
      answer = result

print(answer)
