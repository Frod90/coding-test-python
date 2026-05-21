def solution(sequence, k):
    left, right = 0, 0
    n = len(sequence)
    total = sequence[right]
    answer = [-1, n]
    
    while right < n:
        if total < k:
            right += 1
            if right == n:
                break
            total += sequence[right]
        elif total > k:
            total -= sequence[left]
            left += 1
        else:
            if right - left < answer[1] - answer[0]:
                answer = [left, right]
            
            total -= sequence[left]
            left += 1
        
    return answer