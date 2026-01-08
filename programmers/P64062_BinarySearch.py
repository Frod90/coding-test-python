def _check(stones, k, people_count):
    count = 0
    for stone in stones:
        if stone < people_count:
            count += 1
            if count >= k:
                return False
        else:
            count = 0
    return True
                
def solution(stones, k):
    left, right = 1, max(stones)
    answer = 0
    
    while left <= right:
        mid = (left + right) // 2
        
        if _check(stones, k, mid):
            left = mid + 1
            answer = mid
        else:
            right = mid - 1

    return answer