def solution(order):
    answer = 0
    s = []
    n = len(order)
    
    j = 0
    for i in range(1, n + 1):
        if i == order[j]:
            answer += 1
            j += 1
            continue
        
        while s and s[-1] == order[j]:
            answer += 1
            s.pop()
            j += 1
    
        s.append(i)
        
    while s and s[-1] == order[j]:
        answer += 1
        s.pop()
        j += 1
        
    return answer