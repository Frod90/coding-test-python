def solution(n, money):
    dists = [0] * (n + 1)
    dists[0] = 1
    division = 1_000_000_007
    
    for coin in money:
        for i in range(coin, n + 1):
            dists[i] += dists[i - coin] % division
    return dists[n]