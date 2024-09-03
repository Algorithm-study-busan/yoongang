from collections import deque

def bfs(visited, graph, start):
    q = deque()
    q.append(start)
    visited[start] = True
    
    while q:
        now = q.popleft()
        
        for next in graph[now]:
            if not visited[next]:
                visited[next] = True
                q.append(next)

def solution(n, computers):
    visited = [False] * n
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j: continue
            
            if computers[i][j] == 1:
                graph[i].append(j)
    
    answer = 0
    for i in range(n):
        if not visited[i]:
            bfs(visited, graph, i)
            answer += 1
    
    return answer
