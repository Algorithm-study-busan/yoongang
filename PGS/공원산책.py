def getPosition(park, h, w):
    for i in range(h):
        for j in range(w):
            if park[i][j] == 'S':
                return [i, j]

dirt = {'E': (0, 1), 'S': (1, 0), 'W': (0, -1), 'N': (-1, 0)}

def solution(park, routes):
    h = len(park)
    w = len(park[0])
    answer = getPosition(park, h, w)
    
    for route in routes:
        position = answer
        op, n = route.split(' ')
        d = dirt[op]
        
        temp = True
        for i in range(1, int(n) + 1):
            next_h = position[0] + i * d[0]
            next_w = position[1] + i * d[1]
            
            if next_h >= h or next_h < 0 or next_w >= w or next_w < 0 or park[next_h][next_w] == 'X':
                temp = False
                break
            
        if temp:
            answer = [position[0] + int(n) * d[0], position[1] + int(n) * d[1]]
            
    return answer