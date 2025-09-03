def solution(diffs, times, limit):
    
    def cal(level):
        total_time = times[0]
        for i in range(1, len(diffs)):
            total_time += times[i]
            if diffs[i] > level:
                n = diffs[i] - level
                total_time += n * (times[i] + times[i - 1])
                
            if total_time > limit:
                return False
        
        return total_time <= limit
    
    left, right = 1, max(diffs)
    answer = right
    while left <= right:
        mid = (left + right) // 2
        if cal(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
            
    return answer

from itertools import permutations