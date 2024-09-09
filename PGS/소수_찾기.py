from itertools import permutations 

def is_prime(n):
    if n in [0, 1]: return False

    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            return False
    
    return True

def solution(numbers):
    permutation_nums = []
    for i in range(1, len(numbers) + 1):
        # permutations는 첫 번째 인자로 들어온 이터러블 객체(numbers)에서
        # 두 번째 인자로 들어온 개수(i) 만큼을 선택한 순열을 반환한다.
        permutation_nums += list(permutations(numbers, i)) 
        
    nums = list(set([int(("").join(p)) for p in permutation_nums]))
    
    answer = 0
    for num in nums:
        if is_prime(num):
            answer += 1
            
    return answer
