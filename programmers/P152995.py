def solution(scores):

    answer = 0
    a, b = scores[0]
    
    scores.sort(key=lambda x: (-x[0], x[1]))
    maxi = scores[0][1]
    
    for c, d in scores:
        
        if d < maxi:
            if a == c and b == d:
                return -1
            continue
        
        maxi = d
        
        if c + d > a + b:
            answer += 1

    return answer + 1