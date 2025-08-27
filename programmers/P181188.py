def solution(targets):
    targets.sort(key=lambda x:x[1])
    
    answer = 0
    baseEnd = -1
    for s, e in targets:
        if s >= baseEnd:
            answer += 1
            baseEnd = e
    
    return answer