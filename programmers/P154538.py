from collections import deque

def solution(x, y, n):
    dists = [-1] * (y + 1)
    dists[x] = 0
    q = deque([x])
    
    while q:
        bx = q.popleft()
        if bx == y:
            break
        
        if bx + n <= y and dists[bx + n] == -1:
            dists[bx + n] = dists[bx] + 1
            q.append(bx + n)
        if bx * 2 <= y and dists[bx * 2] == -1:
            dists[bx * 2] = dists[bx] + 1
            q.append(bx * 2)
        if bx * 3 <= y and dists[bx * 3] == -1:
            dists[bx * 3] = dists[bx] + 1
            q.append(bx * 3)
            
    return dists[y]