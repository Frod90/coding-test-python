from collections import deque

def solution(board):
    h, w = len(board), len(board[0])
    dists = [[[float('inf')] * 4 for _ in range(w)] for _ in range(h)]
    directs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    
    q = deque()
    for i in range(4):
        dists[0][0][i] = 0
        q.append((0, 0, i))
    
    while q:
        x, y, d = q.popleft()
        for i, (ex, ey) in enumerate(directs):
            nx, ny = x + ex, y + ey
            cost = 100 if d % 2 == i % 2 else 600
            
            if 0 <= nx < w and 0 <= ny < h:
                if board[ny][nx] == 0:
                    if dists[y][x][d] + cost < dists[ny][nx][i]:
                        dists[ny][nx][i] = dists[y][x][d] + cost
                        q.append((nx, ny, i))

    return min(dists[-1][-1])