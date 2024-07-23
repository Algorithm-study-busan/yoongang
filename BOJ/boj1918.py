string = list(input())
cmd = []
result = ''

for s in string:
  if s.isalpha():
    result += s
  else:
    if s == '(':
      cmd.append(s)
    elif s == '*' or s == '/':
      # 앞에서 * 또는 /이 나왔으면 빼낸다.
      while cmd and (cmd[-1] == '*' or cmd[-1] == '/'):
        result += cmd.pop()
      cmd.append(s)
    elif s == '+' or s == '-':
      # +,-는 우선순위가 가장 낮기 때문에 괄호가 나오는게 아닌 이상 + 또는 -가 나타나면
      # cmd에 존재하는 수식은 모두 빼낸다.
      while cmd and cmd[-1] != '(':
        result += cmd.pop()
      cmd.append(s)
    elif s == ')':
      while cmd and cmd[-1] != '(':
        result += cmd.pop()
      # ( 제거
      cmd.pop()

while cmd:
  c = cmd.pop()
  if c != '(':
    result += c

print(result)
