# 시간초과가 발생하기 때문에 문자열s를 한번 순회하면서 IOI 형태가 반복해서
# 나타나는 횟수가 n번이 되는 경우 result를 1씩 더해주는 방법으로 풀이
n = int(input())
m = int(input())
s = input()

target = 'IOI'
i = 0
cnt = 0
result = 0
while i < m - 1:
  if s[i : i + 3] == target:
    i += 2
    cnt += 1
    if cnt == n:
      result += 1
      # cnt == n이면 두칸 뒤에서 OI가 나오는 경우 상황을 이어가기 위해 cnt를 -1해준다.
      cnt -= 1
  else:
    i += 1
    cnt = 0
  
print(result)
