
def match(m, n, graph):
    visit = set()
    
    for y in range(m - 1):
        for x in range(n - 1):
            if graph[y][x] == '':
                continue
            
            if graph[y][x] == graph[y + 1][x] == graph[y][x + 1] == graph[y + 1][x + 1]:
                visit.add((x, y))
                visit.add((x, y + 1))
                visit.add((x + 1, y))
                visit.add((x + 1, y + 1))
    
    for x, y in visit:
        graph[y][x] = ''
    
    return len(visit)
    
def fill_blank(m, n, graph):
    for x in range(n):
        tmp = []
        
        for y in range(m - 1, -1, -1):
            if graph[y][x]:
                tmp.append(graph[y][x])
        
        index = m - 1
        for block in tmp:
            graph[index][x] = block
            index -= 1
        
        while index >= 0:
            graph[index][x] = ''
            index -= 1

def solution(m, n, board):
    graph = [list(row) for row in board]
    answer = 0
    
    while True:
        deleted_count = match(m, n, graph)
        if deleted_count == 0:
            break

        answer += deleted_count
        fill_blank(m, n, graph)
        
    return answer