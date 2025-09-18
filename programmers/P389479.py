def solution(players, m, k):
    answer = 0
    servers = [0] * 24
    
    for i in range(24):
        servers[i] += servers[i - 1]
        need = players[i] // m
        if servers[i] < need:
            net = need - servers[i]
            servers[i] += net
            answer += net
            
            if i + k < 24:
                servers[i + k] -= net
    
    return answer