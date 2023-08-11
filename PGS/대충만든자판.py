def solution(keymap, targets):
    answer = []
    alp = {}
    for key in keymap:
        for i in range(len(key)):
            if key[i] in alp:
                if i + 1 < alp[key[i]]:
                    alp[key[i]] = i + 1
            else:   
                alp[key[i]] = i + 1
    
    for target in targets:
        count = 0
        for t in target:
            if t not in alp:
                count = -1
                break
            count += alp[t]
        answer.append(count)
            
    return answer