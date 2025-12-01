def solution(info, n, m):
    s = set()
    
    def recur(index, a, b):                
        if a >= n or b >= m or (index, a, b) in s:
            return n
        s.add((index, a, b))
        
        if index == len(info):
            return a
        
        next_a, next_b = a + info[index][0], b + info[index][1]
        use_a = recur(index + 1, next_a, b)
        use_b = recur(index + 1, a, next_b)
        return min(use_a, use_b)

    answer = recur(0, 0, 0)
    if answer == n:
        return -1
    return answer