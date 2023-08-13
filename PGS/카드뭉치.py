def test_cards(cards1, cards2, goal):
    for word in goal:
        if len(cards1) > 0 and cards1[0] == word:
            cards1.pop(0)
            continue
        elif len(cards2) > 0 and cards2[0] == word:
            cards2.pop(0)
        else:
            return False
    
    return True

def solution(cards1, cards2, goal):
    answer = ''
    first = test_cards(cards1, cards2, goal)
    second = test_cards(cards2, cards1, goal)
    
    if first or second:
        answer = 'Yes'
    else:
        answer = 'No'
        
    return answer