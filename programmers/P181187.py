from math import ceil

def solution(r1, r2):
    answer = 0
    high = r2**2
    low = r1**2
    
    for i in range(1, r2 + 1):
        base = i**2
        max_y = int((high - base)**0.5)
        if i >= r1:
            min_y = 0
        else:
            min_y = ceil((low - base)**0.5)

        answer += max_y - min_y + 1
    
    return answer * 4