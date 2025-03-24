
def solution(board, skill):
    
    dist = [[0 for _ in range(len(board[0]) + 1)] for _ in range(len(board) + 1)]
    
    for type, r1, c1, r2, c2, degree in skill:
        
        if type == 1:
            degree *= -1

        dist[r1][c1] += degree
        dist[r2 + 1][c1] -= degree
        dist[r1][c2 + 1] -= degree
        dist[r2 + 1][c2 + 1] += degree
    
    for y in range(len(dist)):
        for x in range(1, len(dist[0])):
            dist[y][x] += dist[y][x - 1]
    
    for x in range(len(dist[0])):
        for y in range(1, len(dist)):
            dist[y][x] += dist[y - 1][x]

    answer = 0
    for y in range(len(board)):
        for x in range(len(board[0])):
            board[y][x] += dist[y][x]
            if board[y][x] > 0:
                answer += 1
    
    return answer 