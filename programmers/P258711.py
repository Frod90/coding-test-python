def solution(edges):
    
    graph = [[0, 0] for _ in range(1_000_001)]
    
    for a, b in edges:
        graph[a][0] += 1
        graph[b][1] += 1
    
    n, nodeNum, stick, eight = 0, 0, 0, 0
    for i in range(1, len(graph)):
        a, b = graph[i]
        
        if a >= 2 and b == 0:
            n = a
            nodeNum = i
        elif a == 0 and b >= 1:
            stick += 1
        elif a == 2 and b >= 2:
            eight += 1
            
    answer = [nodeNum, n - stick - eight, stick, eight]
    return answer
