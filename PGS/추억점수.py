def solution(name, yearning, photo):
    answer = []
    for people in photo:
        count = 0
        for person in people:
            try:
                idx = name.index(person)
                count += yearning[idx]
            except ValueError:
                continue
        answer.append(count)
    return answer