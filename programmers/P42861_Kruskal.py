def solution(n, costs):
    def _find(a):
        if a == parents[a]:
            return a
        
        parents[a] = _find(parents[a])
        return parents[a]
    
    def _union(a, b):
        parentA, parentB = _find(a), _find(b)
        if parentA == parentB:
            return
        
        if ranks[parentA] < ranks[parentB]:
            parents[parentA] = parentB
        elif ranks[parentB] < ranks[parentA]:
            parents[parentB] = parentA
        else:
            parents[parentA] = parentB
            ranks[parentB] += 1
        
    parents = [i for i in range(n)]
    ranks = [0] * n
    
    answer = 0
    costs.sort(key=lambda x:x[2])
    for a, b, c in costs:
        if _find(a) == _find(b):
            continue
            
        _union(a, b)
        answer += c
    return answer