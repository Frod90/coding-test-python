from collections import deque

def solution(bridge_length, weight, truck_weights):
    trucks = deque(truck_weights)
    q = deque()
    time, total_weight = 0, 0
    
    while trucks or q:
        time += 1
        
        if q and time - q[0][1] >= bridge_length:
            pw, pt = q.popleft()
            total_weight -= pw
    
        if trucks and trucks[0] + total_weight <= weight:
            w = trucks.popleft()
            total_weight += w
            q.append((w, time))
    
    return time