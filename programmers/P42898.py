
def solution(m, n, puddles):
    graph = [[True] * (m) for _ in range(n)]
    for x, y in puddles:
        graph[y - 1][x - 1] = False
        
    dists = [[0] * (m) for _ in range(n)]
    for x in range(m):
        if not graph[0][x]:
            break
        dists[0][x] = 1
    for y in range(n):
        if not graph[y][0]:
            break    
        dists[y][0] = 1
    
    division_unit = 1_000_000_007
    for y in range(1, n):
        for x in range(1, m):
            if graph[y][x]:
                dists[y][x] = (dists[y - 1][x] + dists[y][x - 1]) % division_unit

    return dists[n - 1][m - 1]