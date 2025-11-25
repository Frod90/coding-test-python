def solution(n):
    if n < 3:
        return n
    
    dists = [0] * (n + 1)
    dists[1] = 1
    dists[2] = 2
    
    for i in range(3, n + 1):
        dists[i] = (dists[i - 1] + dists[i - 2]) % 1234567
    
    return dists[-1]