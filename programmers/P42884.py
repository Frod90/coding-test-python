def solution(routes):
    routes.sort(key=lambda x:(x[1], x[0]))
    point = -30_001
    answer = 0
    
    for left, right in routes:
        if point < left:
            point = right
            answer += 1
        
    return answer