
answer = [0, 0]

def check(sx, sy, ex, ey, arr):
    base = arr[sy][sx]
    for y in range(sy, ey):
        for x in range(sx, ex):
            if arr[y][x] != base:
                return False
    return True

def _recur(sx, sy, ex, ey, n, arr):
    if n == 1 or check(sx, sy, ex, ey, arr):
        answer[arr[sy][sx]] += 1
        return
    
    n = n // 2
    _recur(sx, sy, sx + n, sy + n, n, arr)
    _recur(sx + n, sy, ex, sy + n, n, arr)
    _recur(sx, sy + n, sx + n, ey, n, arr)
    _recur(sx + n, sy + n, ex, ey, n, arr)
        

def solution(arr):
    n = len(arr)
    _recur(0, 0, n, n, n, arr)
    return answer