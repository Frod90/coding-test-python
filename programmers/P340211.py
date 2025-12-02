
def solution(points, routes):
    d = dict()    
    for route in routes:
        time = 0
        for i in range(len(route) - 1):
            sy, sx = points[route[i] - 1]
            ey, ex = points[route[i + 1] - 1]

            dy = 1 if ey > sy else -1
            for _ in range(abs(ey - sy)):
                d[(time, sy, sx)] = d.get((time, sy, sx), 0) + 1
                time += 1
                sy += dy
            
            dx = 1 if ex > sx else -1
            for _ in range(abs(ex - sx)):
                d[(time, sy, sx)] = d.get((time, sy, sx), 0) + 1
                time += 1
                sx += dx

        y, x = points[route[-1] - 1]
        d[(time, y, x)] = d.get((time, y, x), 0) + 1
    
    answer = 0
    for v in d.values():
        if v > 1:
            answer += 1
    return answer