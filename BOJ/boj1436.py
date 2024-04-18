n = int(input())

num = 665
while n != 0:
  num += 1
  if str(num).find('666') != -1:
    n -= 1
    
print(num)
