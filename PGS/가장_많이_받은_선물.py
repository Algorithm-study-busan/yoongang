def solution(friends, gifts):
    counts = {friend: {friend: 0 for friend in friends} for friend in friends}
    index = {friend: 0 for friend in friends}

    for gift in gifts:
        a, b = gift.split(' ')
        counts[a][b] += 1
        index[a] += 1
        index[b] -= 1

    for a in friends:
        for b in friends:
            if a == b: continue
            
            if counts[a][b] < counts[b][a]:
                counts[b][b] += 1
            elif counts[a][b] > counts[b][a]:
                counts[a][a] += 1
            else:
                if index[a] < index[b]:
                    counts[b][b] += 1
                elif index[a] > index[b]:
                    counts[a][a] += 1
    
    answer = 0
    for friend in friends:
        if counts[friend][friend] > answer:
            answer = counts[friend][friend]
    
    return answer // 2
