def solution(id_list, report, k):
    unique_report = list(set(report))
    answer = [0] * len(id_list)
    report_result = { id: 0 for id in id_list }
    
    # 신고받은 횟수 저장
    for id in unique_report:
        report_result[id.split(' ')[1]] += 1
    
    # 신고받은 횟수가 k 이상이면 신고한 사람의 answer를 +1
    for id in unique_report:
        a, b = id.split(' ')
        if report_result[b] >= k:
            answer[id_list.index(a)] += 1
            
    return answer
