
from math import ceil
from collections import deque

def solution(progresses, speeds):
    q = deque(ceil((100 - progresses[i]) / speeds[i]) for i in range(len(progresses)))
    base_value = q.popleft()
    count = 1
    answer = []
    
    while q:
        if base_value >= q[0]:
            count += 1
            q.popleft()
        else:
            base_value = q.popleft()
            answer.append(count)
            count = 1
    answer.append(count)
    
    return answer