# 힙(힙은 기본적으로 최소힙 구조)
import sys
import heapq

input = sys.stdin.readline

n = int(input())

heap = []
for _ in range(n):
  x = int(input())

  if x == 0:
    if len(heap) == 0:
      print(0)
      continue

    print(heapq.heappop(heap))
  else:
    heapq.heappush(heap, x)

# 우선순위 큐
# import sys
# from queue import PriorityQueue

# input = sys.stdin.readline

# n = int(input())

# q = PriorityQueue()
# for _ in range(n):
#   x = int(input())
#   if x == 0:
#     if q.qsize() == 0:
#       print(0)
#       continue

#     print(q.get())
#   else:
#     q.put(x)
