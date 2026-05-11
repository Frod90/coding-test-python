def solution(elements):
    extend_elements = elements * 2
    s = set()    
    n = len(elements)
    
    for length in range(1, n + 1):
        current = sum(extend_elements[:length])
        s.add(current)
        
        for i in range(1, n):
            current += extend_elements[i + length - 1]
            current -= extend_elements[i - 1]
            s.add(current)
            
    return len(s)