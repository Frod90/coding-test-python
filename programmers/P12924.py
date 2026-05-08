def solution(n):
    left = 1
    right = 1
    total = 0
    end = n // 2
    answer = 1
    
    while left <= end:
        if total < n:
            total += right
            right += 1
        elif total > n:
            total -= left
            left += 1
        else:
            answer += 1
            total -= left
            left += 1
    
    return answer