from itertools import combinations

def solution(n, q, ans):
    nums = [i for i in range(1, n + 1)]
    candidates = list(combinations(nums, 5))
    
    for i in range(len(q)):
        question = q[i]
        ac = ans[i]
        tmp = []
        
        for candi in candidates:
            s = set(question)
            s.update(candi)
            matchCount = 10 - len(s)
            if ac == matchCount:
                tmp.append(candi)
                
        candidates = tmp
        
    return len(candidates)