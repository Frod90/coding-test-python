def solution(grid):
    direct = ((0, 1), (1, 0), (0, -1), (-1, 0))
    dr = {'L':-1, 'R':1, 'S':0}
    
    h, w = len(grid), len(grid[0])
    visit = [[[False] * 4 for _ in range(w)] for _ in range(h)]
    
    answer = []
    for y in range(h):
        for x in range(w):
            for d in range(4):
                if visit[y][x][d]:
                    continue
                
                count = 0
                while not visit[y][x][d]:
                    visit[y][x][d] = True
                    count += 1
                    
                    ex, ey = direct[d]
                    x, y = (x + ex) % w, (y + ey) % h
                    d = (d + dr[grid[y][x]]) % 4
                answer.append(count)
    
    return sorted(answer)