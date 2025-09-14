from collections import deque

def solution(n):
    converter = {
        0 : lambda n : [4, (n - 1) // 3],
        1 : lambda n : [1, n // 3],
        2 : lambda n : [2, n // 3]
    }
    
    q = deque()
    while n > 0:
        num, n = converter[n % 3](n)
        q.appendleft(str(num))
    
    return "".join(q)