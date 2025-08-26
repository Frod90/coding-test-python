from collections import deque

def solution(land):
    def fill(x, y):
        if land[y][x] == 0 or dist[y][x] != 0:
            return
        
        q = deque()
        q.append((x, y))
        mark = set()
        mark.add(x)
        dist[y][x] = 1
        
        count = 1
        while q:
            bx, by = q.popleft()
        
            for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                nx, ny = bx + dx, by + dy
                if 0 <= nx < w and 0 <= ny < h:
                    if land[ny][nx] == 1 and dist[ny][nx] == 0:
                        dist[ny][nx] = 1
                        count += 1
                        mark.add(nx)
                        q.append((nx, ny))
        
        for mx in mark:
            answer[mx] += count
            
    w = len(land[0])
    h = len(land)
    dist = [[0] * w for _ in range(h)]
    answer = [0] * w
    
    for y in range(h):
        for x in range(w):
            fill(x, y)
    
    return max(answer)