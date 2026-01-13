
def solution(n, times):
    def _cal(mid):
        tmp = 0
        for time in times:
            tmp += mid // time
        return tmp
    
    left, right = 1, 1_000_000_000_000_000_000
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        
        if _cal(mid) >= n:
            right = mid - 1
            answer = mid
        else:
            left = mid + 1
        
    return answer