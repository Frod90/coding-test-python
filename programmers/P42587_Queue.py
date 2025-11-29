
from collections import deque

def solution(priorities, location):
    q = deque((i, v) for i, v in enumerate(priorities))
    answer = 0
    
    while q:
        current = q.popleft()
        
        if any(current[1] < other[1] for other in q):
            q.append(current)
        else:
            answer += 1
            if current[0] == location:
                return answer
    
    return answer
