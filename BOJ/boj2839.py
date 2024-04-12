n = int(input())

three = 0
five = n // 5
n %= 5
while True:
  if n == 0 or five < 0: break

  if n % 3 != 0:
    five -= 1
    n += 5
  else:
    three += n // 3
    n = 0
  
if n == 0:
  print(three + five)
else:
  print(-1)
  