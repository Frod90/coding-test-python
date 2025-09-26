def solution(n):
    delta = [[0, 1], [1, 0], [-1, -1]]
    graph = [[0] * i for i in range(1, n + 1)]
    x = d = 0
    y = -1
    count = 1
    
    for w in range(n, 0, -1):
        for i in range(w):
            x += delta[d][0]
            y += delta[d][1]
            graph[y][x] = count
            count += 1
        
        d = (d + 1) % 3
 
    answer = []
    for row in graph:
        answer += row
    return answer