from collections import deque

def solution(storage, requests):
    graph = []
    for row in storage:
        graph.append(list(row))
    
    w = len(graph[0])
    h = len(graph)
    
    def c(mark):
        for y in range(h):
            for x in range(w):
                if graph[y][x] == mark:
                    graph[y][x] = ""
        
    def g(mark):
        q = deque()
        visit = [[False for _ in range(w)] for _ in range(h)]
        tmp = []
        
        for i in range(w):
            if graph[0][i] == "":
                q.append([0, i])
            elif graph[0][i] == mark:
                tmp.append((0, i))
            if graph[h - 1][i] == "":
                q.append([h - 1, i])
            elif graph[h - 1][i] == mark:
                tmp.append((h - 1, i))
                
            visit[0][i] = True
            visit[h - 1][i] = True
        for i in range(h):
            if graph[i][0] == "":
                q.append([i, 0])
            elif graph[i][0] == mark:
                tmp.append((i, 0))
            if graph[i][w - 1] == "":
                q.append([i, w - 1])
            elif graph[i][w - 1] == mark:
                tmp.append((i, w - 1))
        
            visit[i][0] = True
            visit[i][w - 1] = True
        
        while q:
            by, bx = q.popleft()            
            for ey, ex in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                ny, nx = by + ey, bx + ex
                if 0 <= ny < h and 0 <= nx < w and not visit[ny][nx]:
                    visit[ny][nx] = True
                    if graph[ny][nx] == mark:
                        tmp.append((ny, nx))
                    elif graph[ny][nx] == "":
                        q.append([ny, nx])
                        
        for y, x in tmp:
            graph[y][x] = ""
        
    for r in requests:
        if len(r) == 2:
            c(r[0])
        else:
            g(r)

    count = 0
    for row in graph:
        count += row.count("")
    
    return w * h - count