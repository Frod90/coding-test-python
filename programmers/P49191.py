def solution(n, results):
    res = [[-1] * n for _ in range(n)]
    for a, b in results:
        a -= 1
        b -= 1
        res[a][b] = 1
        res[b][a] = 0
    
    for k in range(n):
        for y in range(n):
            for x in range(n):
                if y != x and res[y][x] == -1:
                    if res[y][k] == 1 and res[k][x] == 1:
                        res[y][x] = 1
                    elif res[y][k] == 0 and res[k][x] == 0:
                        res[y][x] = 0
    
    answer = 0            
    for row in res:
        if row.count(1) + row.count(0) == n - 1:
            answer += 1
    return answer