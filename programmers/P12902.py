
def solution(n):
    if n % 2 == 1:
        return 0
    
    dists = [0] * (n + 1)
    dists[0], dists[2] = 1, 3
    for i in range(4, n + 1, 2):
        dists[i] = dists[i - 2] * 3
        for j in range(i - 4, -1, -2):
            dists[i] += dists[j] * 2
        dists[i] %= 1_000_000_007
        
    return dists[n]