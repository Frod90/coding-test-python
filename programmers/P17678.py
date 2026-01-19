from collections import deque

def solution(n, t, m, timetable):
    def toString(time):
        hour = time // 60
        minute = time - hour * 60
        str_hour = str(hour) if hour >= 10 else "0" + str(hour)
        str_minute = str(minute) if minute >= 10 else "0" + str(minute)
        return str_hour + ":" + str_minute
    
    arr = []
    for time_info in timetable:
        time = int(time_info[:2]) * 60 + int(time_info[3:])
        arr.append(time)
    arr.sort()
    q = deque(arr)
    
    result = [[] for _ in range(n)]    
    time = 9 * 60
    for i in range(n):
        for j in range(m):
            if q and q[0] <= time:
                result[i].append(q.popleft())
            else:
                break
        time += t
    
    arr = result[-1]
    if len(arr) == m:
        return toString(arr.pop() - 1)
    return toString(time - t)