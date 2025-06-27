
def solution(cap, n, deliveries, pickups):
    answer = 0
    
    di, pi = n - 1, n - 1
    
    while di >= 0 or pi >= 0:
        
        while di >= 0 and deliveries[di] == 0:
            di -= 1
        while pi >= 0 and pickups[pi] == 0:
            pi -= 1
            
        fi = max(di, pi) + 1
        if fi == 0:
            break
        answer += fi * 2
        
        dc, pc = cap, cap
        while di >= 0 and dc > 0:
            if deliveries[di] <= dc:
                dc -= deliveries[di]
                deliveries[di] = 0
                di -= 1
            else:
                deliveries[di] -= dc
                dc = 0
        while pi >= 0 and pc > 0:
            if pickups[pi] <= pc:
                pc -= pickups[pi]
                pickups[pi] = 0
                pi -= 1
            else:
                pickups[pi] -= pc
                pc = 0        
    
    return answer