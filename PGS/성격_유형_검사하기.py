def solution(survey, choices):
    category = {ctg: 0 for ctg in ["RT", "CF", "JM", "AN"]}
    
    for i in range(len(survey)):
        if choices[i] == 4: continue
        
        if survey[i] == ''.join(sorted(survey[i])):
            category[survey[i]] += choices[i] - 4
        else:
            category[''.join(sorted(survey[i]))] -= choices[i] - 4
    
    answer = ''
    for key, value in category.items():
        if value <= 0:
            answer += key[0]
        else:
            answer += key[1]
            
    return answer
