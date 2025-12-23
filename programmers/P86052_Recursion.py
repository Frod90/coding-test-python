import sys
sys.setrecursionlimit(500*500*4)

direct = {
    'S': ((0, 1, 0), (-1, 0, 1), (0, -1, 2), (1, 0, 3)),
    'L': ((1, 0, 3), (0, 1, 0), (-1, 0, 1), (0, -1, 2)),
    'R': ((-1, 0, 1), (0, -1, 2), (1, 0, 3), (0, 1, 0))
}

def cal(grid, visit, sx, sy, sd, cx, cy, bd, count):
    ex, ey, nd = direct[grid[cy][cx]][bd]
    nx, ny = (cx + ex) % len(grid[0]), (cy + ey) % len(grid)
    
    if sx == cx and sy == cy and sd == nd:
        return count
    
    if not visit[ny][nx][nd]:
        visit[ny][nx][nd] = True
        return cal(grid, visit, sx, sy, sd, nx, ny, nd, count + 1)

    return 0
    
def solution(grid):
    visit = [[[False] * 4 for _ in range(len(grid[0]))] for _ in range(len(grid))]

    answer = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            for ex, ey, d in ((0, 1, 0), (-1, 0, 1), (0, -1, 2), (1, 0, 3)):
                nx, ny = (x + ex) % len(grid[0]), (y + ey) % len(grid)
                if not visit[ny][nx][d]:
                    visit[ny][nx][d] = True
                    count = cal(grid, visit, x, y, d, nx, ny, d, 1)
                    
                    if count != 0:
                        answer.append(count)
    
    return sorted(answer)