
import heapq

def solution(operations):
    lower_q = []
    upper_q = []
    d = dict()
    
    for command in operations:
        c = command[0]
        num = int(command[2:])
        
        if c == 'I':
            heapq.heappush(lower_q, num)
            heapq.heappush(upper_q, -num)
            d[num] = d.get(num, 0) + 1
        elif num == 1:
            while upper_q:
                p = -heapq.heappop(upper_q)
                if d.get(p, 0) > 0:
                    d[p] -= 1
                    if d[p] <= 0:
                        del d[p]
                    break
        elif num == -1:
            while lower_q:
                p = heapq.heappop(lower_q)
                if d.get(p, 0) > 0:
                    d[p] -= 1
                    if d[p] <= 0:
                        del d[p]
                    break

    maxi = 0
    while upper_q:
        p = -heapq.heappop(upper_q)
        if p in d:
            maxi = p
            break

    mini = 0
    while lower_q:
        p = heapq.heappop(lower_q)
        if p in d:
            mini = p
            break
    
    return [maxi, mini]