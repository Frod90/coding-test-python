def solution(land):
    dists = [[0] * len(land[0]) for _ in range(len(land))]
    for x in range(len(land[0])):
        dists[-1][x] = land[-1][x]
    
    for y in range(len(land) - 2, -1, -1):
        first, second = 0, 0
        for v in dists[y + 1]:
            if v > first:
                second = first
                first = v
            elif v > second:
                second = v
        
        for x in range(len(land[0])):
            if dists[y + 1][x] == first:
                dists[y][x] = land[y][x] + second
            else:
                dists[y][x] = land[y][x] + first
    
    return max(dists[0])