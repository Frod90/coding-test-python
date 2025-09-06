def solution(board):
    h = len(board)
    w = len(board[0])
    
    dp = [[0] * w for _ in range(h)]
    for i in range(w):
        dp[0][i] = board[0][i]
    for i in range(h):
        dp[i][0] = board[i][0]
    
    for y in range(1, h):
        for x in range(1, w):
            if board[y][x] == 1:
                dp[y][x] = min(dp[y][x - 1], dp[y - 1][x], dp[y - 1][x - 1]) + 1
    
    length = 0
    for row in dp:
        length = max(length, max(row))
                                
    return length**2