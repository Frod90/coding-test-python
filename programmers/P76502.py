
from collections import deque

def isA(string):
    st = []
    pair = {')':'(', '}':'{', ']':'['}
    
    for digit in string:
        if digit in "[{(":
            st.append(digit)
            continue
            
        if not st or pair[digit] != st[-1]:
            return False

        st.pop()
    
    return len(st) == 0

def solution(s):
    if len(s) % 2 != 0:
        return 0
    
    answer = 0
    q = deque(s)
    for i in range(len(s)):
        if isA(q):
            answer += 1
        q.append(q.popleft())
    return answer