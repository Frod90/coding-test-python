from collections import defaultdict, Counter

def solution(weights):
    d = defaultdict(int)
    c = Counter(weights)
    
    answer = 0
    for w in c.keys():
        count = c[w]
        if count > 1:
            answer += count * (count - 1) // 2
            
        for i in range(2, 5):
            answer += count * d.get(w * i, 0)
            d[w * i] += count
            
    return answer