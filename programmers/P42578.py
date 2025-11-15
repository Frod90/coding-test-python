from itertools import permut

from collections import defaultdict

def solution(clothes):
    d = defaultdict(int)
    for _, cloth_type in clothes:
        d[cloth_type] += 1
    
    answer = 1
    for v in d.values():
        answer *= (v + 1)

    return answer - 1