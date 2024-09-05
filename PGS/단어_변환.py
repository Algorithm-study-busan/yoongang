from collections import deque

def check(w1, w2):
    cnt = 0
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            cnt += 1
    
    return 1 if cnt == 1 else 0

def bfs(begin, target, words):
    visited = [False] * len(words)
    q = deque()
    q.append((begin, 0))
    
    while q:
        now, cnt = q.popleft()
        
        if now == target:
            return cnt
        
        for i in range(len(words)):
            if not visited[i] and check(now, words[i]):
                visited[i] = True
                q.append((words[i], cnt + 1))

def solution(begin, target, words):
    if target not in words: return 0
    
    return bfs(begin, target, words)
