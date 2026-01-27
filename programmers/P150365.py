from collections import deque

def solution(n, m, x, y, r, c, k):
    directs = [(0, 1), (-1, 0), (1, 0), (0, -1)]
    signs = ['d', 'l', 'r', 'u']
    
    dist = abs(r - x) + abs(c - y)
    if dist > k or abs(dist - k) % 2 == 1:
        return "impossible"
    
    cx, cy = x, y
    answer = []
    for step in range(k):
        for i in range(4):
            ey, ex = directs[i]
            nx, ny = cx + ex, cy + ey
            if nx <= 0 or n < nx or ny <= 0 or m < ny:
                continue
                
            dist = abs(r - nx) + abs(c - ny)
            rest = k - step - 1
            if dist > rest:
                continue
            if abs(dist - rest) % 2 == 1:
                continue
        
            cx, cy = nx, ny
            answer.append(signs[i])
            break
    
    return "".join(answer)