from math import ceil

def solution(n, stations, w):
    point = 1
    length = w * 2 + 1

    answer = 0
    for s in stations:
        left = s - w
        if point < left:
            answer += ceil((left - point) / length)
        point = s + w + 1

    if point <= n:
        answer += ceil((n + 1 - point) / length)

    return answer