
from collections import Counter

def solution(want, number, discount):
    d = dict(zip(want, number))
    tmp = Counter(discount[:10])
    answer = 0
    if tmp == d:
        answer += 1
    
    for i in range(10, len(discount)):
        b_key, n_key = discount[i - 10], discount[i]
        
        tmp[b_key] -= 1
        if tmp[b_key] == 0:
            del tmp[b_key]
        tmp[n_key] += 1
        
        if tmp == d:
            answer += 1
    
    return answer