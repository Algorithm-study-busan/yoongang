n = int(input())

times = []
for _ in range(n):
  times.append(list(map(int, input().split(' '))))
# 시작, 종료 시간이 동일한 회의가 존재하는 경우
# 시작 시간 순으로 정렬되어야 해당(시작, 종료 시간이 동일한 회의) 회의를 추가로 진행할 수 있다.
times.sort(key=lambda time: (time[1], time[0]))

count = 0
endTime = 0
for start, end in times:
  if endTime <= start:
    count += 1
    endTime = end

print(count)
