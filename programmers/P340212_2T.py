def cal(diffs, times, limit, level):
    total_time = 0
    time_prev = 0
    
    for i in range(len(diffs)):
        diff = diffs[i]
        time = times[i]
        if diff <= level:
            total_time += time
        else:
            total_time += time + (diff - level) * (time + time_prev)
        
        if total_time > limit:
            return False
        time_prev = time
    
    return True


def solution(diffs, times, limit):
    answer = 0
    left, right = 1, 100_000
    
    while left <= right:
        mid = (left + right) // 2
        if cal(diffs, times, limit, mid):
            right = mid - 1
            answer = mid
        else:
            left = mid + 1
    
    return answer