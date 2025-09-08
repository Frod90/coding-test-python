def solution(places):
    def isAvailable(x, y, graph, h, w):
        deltas = [
            [[-1, 0], [-1, -1], [-2, 0], [-1, 1]],
            [[0, 1], [-1, 1], [0, 2], [1, 1]],
            [[1, 0], [1, -1], [2, 0], [1, 1]],
            [[0, -1], [-1, -1], [0, -2], [1, -1]]
        ]
        
        for delta in deltas:
            dy, dx = delta[0]
            ny, nx = y + dy, x + dx
            if ny < 0 or h <= ny or nx < 0 or w <= nx:
                continue
            if graph[ny][nx] == 'X':
                continue
            if graph[ny][nx] == 'P':
                return False
            
            for i in range(1, 4):
                dy, dx = delta[i]
                ny, nx = y + dy, x + dx
                if 0 <= ny < h and 0 <= nx < w:
                    if graph[ny][nx] == 'P':
                        return False
        return True
    
    def checkPlace(place):
        h, w = len(place), len(place[0])
        for y in range(h):
            for x in range(w):
                if place[y][x] == 'P' and not isAvailable(x, y, place, h, w):
                    return False
    
        return True
    
    answer = []
    for place in places:
        if checkPlace(place):
            answer.append(1)
        else:
            answer.append(0)
    
    return answer