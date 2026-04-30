def solution(target):
    INF = float('inf')
    dists = [[INF, 0] for _ in range(target + 1)]
    dists[0][0] = 0
    
    candidates = []
    candidates.append((50, 1))
    for score in range(1, 21):
        candidates.append((score, 1))
        candidates.append((score * 2, 0))
        candidates.append((score * 3, 0))
    
    for i in range(1, target + 1):
        for score, bonus in candidates:
            if i - score < 0:
                continue
            
            prev_score = dists[i - score][0] + 1
            prev_bonus = dists[i - score][1] + bonus
            
            if prev_score < dists[i][0]:
                dists[i][0] = prev_score
                dists[i][1] = prev_bonus
            elif prev_score == dists[i][0]:
                dists[i][1] = max(dists[i][1], prev_bonus)
            
    answer = dists[target]
    return answer