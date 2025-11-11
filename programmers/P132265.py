from collections import Counter

def solution(topping):
    d = dict(Counter(topping))
    base_length = len(d)
    other = set()

    answer = 0
    for t in topping:
        other.add(t)
        d[t] -= 1
        if d[t] <= 0:
            base_length -= 1
        
        if base_length == len(other):
            answer += 1

    return answer