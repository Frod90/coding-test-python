def solution(sticker):
    n = len(sticker)
    if n <= 3:
        return max(sticker)
    
    dists_use_0 = [0] * (n - 1)
    dists_use_0[0] = sticker[0]
    dists_use_0[1] = sticker[0]
    for i in range(2, n - 1):
        dists_use_0[i] = max(dists_use_0[i - 1], dists_use_0[i - 2] + sticker[i])
    
    dists_not_use_0 = [0] * n
    dists_not_use_0[0] = 0
    dists_not_use_0[1] = sticker[1]
    for i in range(2, n):
        dists_not_use_0[i] = max(dists_not_use_0[i - 1], dists_not_use_0[i - 2] + sticker[i])

    return max(dists_use_0[-1], dists_not_use_0[-1])