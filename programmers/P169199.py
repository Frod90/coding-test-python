from collections import deque

def find_start(board, w, h):
    for y in range(h):
        for x in range(w):
            if board[y][x] == 'R':
                return x, y
    return 0, 0
    
def move(x, y, dx, dy, board, w, h):
    nx, ny = x, y
    while 0 <= nx + dx < w and 0 <= ny + dy < h and board[ny + dy][nx + dx] != 'D':
        nx += dx
        ny += dy
    return nx, ny

def bfs(sx, sy, board, w, h):
    dists = [[0] * w for _ in range(h)]
    dists[sy][sx] = 1
    q = deque()
    q.append([sx, sy])
    
    while q:
        bx, by = q.popleft()
        
        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nx, ny = move(bx, by, dx, dy, board, w, h)
            if bx == nx and by == ny:
                continue
            if dists[ny][nx] != 0:
                continue
            if board[ny][nx] == 'G':
                return dists[by][bx]
            dists[ny][nx] = dists[by][bx] + 1
            q.append([nx, ny])

    return -1    

def solution(board):
    w, h = len(board[0]), len(board)
    sx, sy = find_start(board, w, h)    
    return bfs(sx, sy, board, w, h)