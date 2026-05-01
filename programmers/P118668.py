def solution(alp, cop, problems):
    n = len(problems)
    max_alp = max(problems[i][0] for i in range(n))
    max_cop = max(problems[i][1] for i in range(n))
    
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    
    INF = float('inf')
    dists = [[INF] * (max_cop + 1) for _ in range(max_alp + 1)]
    dists[alp][cop] = 0

    for a in range(alp, max_alp + 1):
        for c in range(cop, max_cop + 1):
            if dists[a][c] == INF:
                continue
            
            if a + 1 <= max_alp:
                dists[a + 1][c] = min(dists[a + 1][c], dists[a][c] + 1)
            if c + 1 <= max_cop:
                dists[a][c + 1] = min(dists[a][c + 1], dists[a][c] + 1)
            
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if a < alp_req or c < cop_req:
                    continue
                
                next_a = min(max_alp, a + alp_rwd)
                next_c = min(max_cop, c + cop_rwd)
                dists[next_a][next_c] = min(dists[next_a][next_c], dists[a][c] + cost)
    
    answer = dists[max_alp][max_cop]
    return answer