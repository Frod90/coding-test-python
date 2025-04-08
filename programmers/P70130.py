from collections import Counter 

def _find(i, a):
    
    arr = []
    count = 0
    for b in a:
        if b != i and (i in arr or not arr):
            arr.append(b)
        if b == i and i not in arr:
            arr.append(b)
            
        if len(arr) >= 2:
            count += 1
            arr = []
        
    return count

def solution(a):
    answer = 0
    counter = Counter(a)
    
    for b in counter.keys():
        if counter[b] * 2 <= answer:
            continue
        
        answer = max(answer, _find(b, a) * 2)
        
    return answer