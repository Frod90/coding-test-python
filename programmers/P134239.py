def solution(k, ranges):
    num = k
    heights = [num]
    while num > 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
        heights.append(num)
    
    areas = [0]
    for i in range(1, len(heights)):
        area = (heights[i] + heights[i - 1]) / 2 + areas[-1]
        areas.append(area)
    
    answer = []
    n = len(areas)
    for a, b in ranges:
        start, end = a, n + b - 1
        if start > end:
            answer.append(-1.0)
        else:
            answer.append(areas[end] - areas[start])
            
    return answer