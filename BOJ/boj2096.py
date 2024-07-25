n = int(input())

max_score = [0] * 3
min_score = [0] * 3
for _ in range(n):
  a, b, c = map(int, input().split())

  max_score = [max(max_score[:2]) + a, max(max_score) + b, max(max_score[1:]) + c]
  min_score = [min(min_score[:2]) + a, min(min_score) + b, min(min_score[1:]) + c]

print(max(max_score), min(min_score))
