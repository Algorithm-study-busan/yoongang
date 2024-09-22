def count(arr, target):
    result = 0
    for n in arr:
        if n >= target:
            result += 1
    
    return result

def solution(citations):
    citations.sort()
    
    start = 0
    end = 10000

    while start <= end:
        mid = (start + end) // 2

        if count(citations, mid) >= mid:
            start = mid + 1
        else:
            end = mid - 1
    
    return start - 1
