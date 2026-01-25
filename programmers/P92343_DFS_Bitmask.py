def solution(info, edges):
    n = len(info)
    links = [0] * n
    for parent, child in edges:
        links[parent] |= (1 << child)
    
    def recur(sheep, wolf, candidates):
        nonlocal answer
        answer = max(answer, sheep)
        
        mask = candidates
        while mask:
            next_bit = mask & -mask
            next_node = next_bit.bit_length() - 1
            mask -= next_bit
            
            ns, nw = sheep, wolf
            if info[next_node] == 1:
                nw += 1
            else:
                ns += 1
            
            if ns > nw:
                next_candidates = (candidates - next_bit) | links[next_node]
                recur(ns, nw, next_candidates)
    
    answer = 0
    recur(0, 0, 1)
    return answer