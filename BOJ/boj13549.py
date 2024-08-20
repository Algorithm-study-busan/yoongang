import heapq

MAX = 100_001
INF = int(1e9)

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist: continue

    for next in (now + 1, now - 1, now * 2):
      cost = dist + 1

      if next == now * 2:
        cost -= 1

      if 0 <= next < MAX and cost < distance[next]:
        distance[next] = cost
        heapq.heappush(q, (cost, next))

n, k = map(int, input().split())

distance = [INF] * MAX
# 가장 짧은 거리의 지점부터 순회하기 위해 우선순위 큐 사용
dijkstra(n)
print(distance[k])
