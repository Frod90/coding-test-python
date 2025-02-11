def solution(triangle):
    answer = 0
    
    visit = [0] * (len(triangle) + 1)
    
    for i in range(len(triangle) - 1, -1, -1):
        rows = triangle[i]
        
        for j in range(len(rows)):
            visit[j] = rows[j] + max(visit[j], visit[j + 1])
    
    return visit[0]