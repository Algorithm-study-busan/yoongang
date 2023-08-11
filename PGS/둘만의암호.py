def solution(s, skip, index):
    answer = ''
    alpha = list('abcdefghijklmnopqrstuvwxyz')
    for i in skip:
        alpha.pop(alpha.index(i))

    for c in s:
        idx = alpha.index(c)
        if idx + index >= len(alpha):
            idx = (idx + index) % len(alpha)
        else:
            idx += index
        answer += alpha[idx]
    
    return answer