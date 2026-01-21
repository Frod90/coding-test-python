def solution(a):
    n = len(a)
    INF = float('inf')

    left_min = [INF] * n
    left_min[0] = a[0]
    for i in range(1, n):
        left_min[i] = min(left_min[i - 1], a[i])

    right_min = [INF] * n
    right_min[n - 1] = a[n - 1]
    for i in range(n - 2, -1, -1):
        right_min[i] = min(right_min[i + 1], a[i])
        
    answer = 2
    for i in range(1, n - 1):
        if left_min[i - 1] > a[i] or a[i] < right_min[i + 1]:
            answer += 1
    return answer


import math
math.factorial