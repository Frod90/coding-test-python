from collections import deque

def _bfs(maps, sx, sy, target_mark):
    w, h = len(maps[0]), len(maps)
    q = deque()
    q.append([sx, sy])
    dists = [[0] * w for _ in range(h)]
    dists[sy][sx] = 1
    
    while q:
        bx, by = q.popleft()
        
        for ex, ey in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nx, ny = bx + ex, by + ey
            if 0 <= nx < w and 0 <= ny < h:
                if maps[ny][nx] == target_mark:
                    return dists[by][bx]
                
                if maps[ny][nx] != 'X' and dists[ny][nx] == 0:
                    dists[ny][nx] = dists[by][bx] + 1
                    q.append([nx, ny])
                    
    return -1

def solution(maps):
    sx, sy, lx, ly = 0, 0, 0, 0
    for y in range(len(maps)):
        for x in range(len(maps[0])):
            if maps[y][x] == 'S':
                sx, sy = x, y
            elif maps[y][x] == 'L':
                lx, ly = x, y
    
    lt = _bfs(maps, sx, sy, 'L')
    if lt == -1:
        return -1
    et = _bfs(maps, lx, ly, 'E')
    if et == -1:
        return -1
    
    return lt + et