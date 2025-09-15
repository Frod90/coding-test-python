import heapq

from collections import defaultdict

def solution(n, k, enemy):
    q = []
    for i, en in enumerate(enemy):
        n -= en
        heapq.heappush(q, -en)
        
        while n < 0 and q and k > 0:
            k -= 1
            n += -heapq.heappop(q)
        
        if n < 0:
            return i
        
    dic = defaultdict(int)
    dic['a'] = 1
    dic['b'] = 3
    dic['c'] = 2

    dic.values
    sorted(dic)

    

    return len(enemy)