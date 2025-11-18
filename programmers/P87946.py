
from itertools import permutations

def solution(k, dungeons):
    answer = 0
    for per in permutations(dungeons):

        tmp, count = k, 0
        for mini, consu in per:
            if tmp < mini:
                break
            tmp -= consu
            count += 1
        answer = max(answer, count)
    
    return answer