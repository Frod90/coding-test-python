import heapq

def solution(n, works):
    q = [-work for work in works]
    heapq.heapify(q)
    while n > 0 and q:
        n -= 1
        p = heapq.heappop(q)
        p += 1
        if p < 0:
            heapq.heappush(q, p)
    
    answer = sum((-work)**2 for work in q)
    return answer