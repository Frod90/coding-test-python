
def solution(n, left, right):  
    start_depth, start_index = left // n, left % n
    end_depth, end_index = right // n, right % n
    
    answer = []
    if start_depth == end_depth:
        for i in range(start_index, end_index + 1):
            answer.append(max(start_depth + 1, i + 1))
        return answer
    
    for i in range(start_index, n):
        answer.append(max(start_depth + 1, i + 1))
    
    start_depth += 1
    while start_depth < end_depth:
        for i in range(n):
            answer.append(max(start_depth + 1, i + 1))
        start_depth += 1
    
    for i in range(end_index + 1):
        answer.append(max(start_depth + 1, i + 1))
    
    return answer