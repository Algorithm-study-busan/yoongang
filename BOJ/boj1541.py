strs = input().split('-')

result = 0
for i in range(len(strs)):
  str = strs[i].split('+')

  if i == 0:
    for num in str:
      result += int(num)
  else:
    for num in str:
      result -= int(num)

print(result)
