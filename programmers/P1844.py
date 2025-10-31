from collections import deque

def solution(maps):
    dists = [[-1] * len(maps[0]) for _ in range(len(maps))]
    dists[0][0] = 1
    q = deque()
    q.append([0, 0])
    
    while q:
        bx, by = q.popleft()
        for ex, ey in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nx, ny = bx + ex, by + ey
            if 0 <= nx < len(maps[0]) and 0 <= ny < len(maps):
                if maps[ny][nx] == 1 and dists[ny][nx] == -1:
                    dists[ny][nx] = dists[by][bx] + 1
                    q.append([nx, ny])
                    
    return dists[-1][-1]