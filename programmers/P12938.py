
def solution(n, s):
    if n > s:
        return [-1]
    
    v = s // n
    answer = [v] * n
    
    rest = s % n
    i = n - 1
    while rest > 0:
        answer[i] += 1
        rest -= 1
        i -= 1
        
    return answer