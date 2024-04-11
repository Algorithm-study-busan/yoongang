import sys

# sys.stdin.readine은 입력을 한 번에 읽어와 저장하기 때문에 입력 하나씩 읽어와
# 저장하는 input보다 빠르다.
# 하지만 input과 다르게 개행문자를 제거해주지 않는다.
input = sys.stdin.readline

string = list(input().strip())
string2 = []
for _ in range(int(input())):
  command = input().strip().split(' ')
  type = command[0]

  if type == 'P':
    string.append(command[1])
  elif type == 'L':
    if len(string) > 0:
      string2.append(string.pop())
  elif type == 'D':
    if len(string2) > 0:
      string.append(string2.pop())
  elif type == 'B':
    if len(string) > 0:
      string.pop()

string2.reverse()
print(''.join(string + string2))
