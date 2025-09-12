from collections import deque

def solution(rows, columns, queries):
    def rotate(x1, y1, x2, y2, graph):
        indexs = deque()
        values = deque()
        
        for x in range(x1, x2):
            indexs.append([x, y1])
            values.append(graph[y1][x])
        for y in range(y1, y2):
            indexs.append([x2, y])
            values.append(graph[y][x2])
        for x in range(x2, x1, -1):
            indexs.append([x, y2])
            values.append(graph[y2][x])
        for y in range(y2, y1, -1):
            indexs.append([x1, y])
            values.append(graph[y][x1])
        
        minValue = min(values)
        indexs.append(indexs.popleft())
        
        for x, y in indexs:
            graph[y][x] = values.popleft()

        return minValue
    
    graph = [[0] * columns for _ in range(rows)]
    count = 1
    for y in range(rows):
        for x in range(columns):
            graph[y][x] = count
            count += 1
    
    answer = []
    for y1, x1, y2, x2 in queries:
        answer.append(rotate(x1 - 1, y1 - 1, x2 - 1, y2 - 1, graph))
    return answer