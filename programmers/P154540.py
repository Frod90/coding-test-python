from collections import deque

def solution(maps):
    def _f(x, y, maps, visit, w, h):        
        q = deque()
        q.append([x, y])
        value = int(maps[y][x])
        visit[y][x] = True
        
        while q:
            bx, by = q.popleft()
            for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                nx, ny = bx + dx, by + dy
                if 0 <= nx < w and 0 <= ny < h and maps[ny][nx] != 'X' and not visit[ny][nx]:
                    visit[ny][nx] = True
                    value += int(maps[ny][nx])
                    q.append([nx, ny])
                    
        return value
        
    w, h = len(maps[0]), len(maps)
    visit = [[False] * w for _ in range(h)]
    answer = []
    for y in range(h):
        for x in range(w):
            if maps[y][x] != 'X' and not visit[y][x]:
                value = _f(x, y, maps, visit, w, h)
                answer.append(value)
    
    if answer:
        answer.sort()
        return answer
    
    return [-1]