def solution(info, edges):
    def recur(sheep, wolf, candidates):
        nonlocal answer
        answer = max(answer, sheep)
        
        for next_node in candidates:
            s, w = sheep, wolf
            if info[next_node] == 1:
                w += 1
            else:
                s += 1
            
            if s > w:
                next_candidates = candidates.copy()
                next_candidates.remove(next_node)
                next_candidates.update(links[next_node])
                recur(s, w, next_candidates)
    
    n = len(info)
    links = [[] for _ in range(n)]
    for parent, child in edges:
        links[parent].append(child)
    
    answer = 0
    candidate = set()
    candidate.add(0)
    recur(0, 0, candidate)
    return answer