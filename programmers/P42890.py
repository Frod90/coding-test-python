from itertools import combinations

def is_candidate(indexs, relation):
    s = set()
    for row in relation:
        s.add(tuple(row[i] for i in indexs))
    return len(s) == len(relation)

def has_subset(indexs, key_set):
    max_size = len(indexs)
    for size in range(1, max_size):
        for combi in combinations(indexs, size):
            if combi in key_set:
                return True
    return False

def solution(relation):
    n = len(relation[0])
    indexs = [i for i in range(n)]
    key_set = set()
    answer = 0
    
    for size in range(1, n + 1):
        for combi in combinations(indexs, size):
            if not has_subset(combi, key_set) and is_candidate(combi, relation):
                answer += 1
                key_set.add(combi)
    
    return answer