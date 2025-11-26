
from collections import Counter

def solution(k, tangerine):
    c = Counter(tangerine)
    answer = 0
    for count in sorted(c.values(), reverse = True):
        k -= count
        answer += 1
        
        if k <= 0:
            break
            
    return answer