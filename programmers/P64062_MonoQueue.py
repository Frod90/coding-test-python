
from collections import deque

def solution(stones, k):
    q = deque(sorted([(stones[i], i) for i in range(k)], key=lambda x:-x[0]))
    answer = q[0][0]
    
    for i in range(k, len(stones)):
        while q and q[0][1] <= i - k:
            q.popleft()
        while q and q[-1][0] < stones[i]:
            q.pop()

        q.append((stones[i], i))
        answer = min(answer, q[0][0])

    return answer