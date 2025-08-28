def isBingo(graph, sign):
    indexs = [
        [[0, 0], [0, 1], [0, 2]],
        [[1, 0], [1, 1], [1, 2]],
        [[2, 0], [2, 1], [2, 2]],
        
        [[0, 0], [1, 0], [2, 0]],
        [[0, 1], [1, 1], [2, 1]],
        [[0, 2], [1, 2], [2, 2]],
        
        [[0, 0], [1, 1], [2, 2]],
        [[0, 2], [1, 1], [2, 0]]
    ]
    
    for index in indexs:
        isMatch = True
        for y, x in index:
            if graph[y][x] != sign:
                isMatch = False
                break
        
        if isMatch:
            return True

def isAvailable(graph):
    oCount = 0
    xCount = 0
    for row in graph:
        oCount += row.count('O')
        xCount += row.count('X')
    
    if oCount < xCount or oCount - xCount > 1:
        return 0
    
    oBingo = isBingo(graph, 'O')
    xBingo = isBingo(graph, 'X')
    
    if oBingo and xBingo:
        return 0
    if oBingo and oCount - xCount != 1:
        return 0
    if xBingo and oCount != xCount:
        return 0
    
    return 1

def solution(board):
    graph = []
    for row in board:
        graph.append(list(row))
    
    return isAvailable(graph)