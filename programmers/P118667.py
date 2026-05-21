from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    count = 0
    max_count = max(len(queue1), len(queue2)) * 3
    
    while count < max_count:
        if sum1 < sum2:
            v = q2.popleft()
            q1.append(v)
            sum1 += v
            sum2 -= v
        elif sum2 < sum1:
            v = q1.popleft()
            q2.append(v)
            sum1 -= v
            sum2 += v
        else:
            return count
        count += 1

    return -1