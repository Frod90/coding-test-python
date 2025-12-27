def solution(n, computers):
    def _find(node):
        if parents[node] == node:
            return node
        
        parents[node] = _find(parents[node])
        return parents[node]
        
    def _union(a, b):
        parent_a, parent_b = _find(a), _find(b)
        
        if parent_a == parent_b:
            return
        
        if ranks[parent_a] > ranks[parent_b]:
            parents[parent_b] = parent_a
        elif ranks[parent_a] > ranks[parent_b]:
            parents[parent_a] = parent_b
        else:
            parents[parent_a] = parent_b
            ranks[parent_b] += 1
    
    parents = [i for i in range(n)]
    ranks = [0] * n
    
    for i in range(n):
        for j in range(i + 1, n):
            if computers[i][j] == 1:
                _union(i, j)
    
    answer = 0
    for i in range(n):
        if i == parents[i]:
            answer += 1
    return answer