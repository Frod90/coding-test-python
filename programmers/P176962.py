def solution(plans):
    p = []
    for name, start, playtime in plans:
        tmp = start.split(":")
        start = int(tmp[0]) * 60 + int(tmp[1])
        p.append([name, start, int(playtime)])
    p.sort(key=lambda x:x[1])
    
    answer = []
    s = []
    for i in range(1, len(p)):
        name, start, playtime = p[i]
        bn, bs, bp = p[i - 1]
        
        rest = start - bs - bp
        if rest < 0:
            s.append([bn, bs + bp - start])
        else:
            answer.append(bn)
            while s and rest > 0:
                sn, sr = s.pop()
                if sr > rest:
                    s.append([sn, sr - rest])
                    rest = 0
                else:
                    answer.append(sn)
                    rest -= sr
    
    answer.append(p[-1][0])
    while s:
        sn, sr = s.pop()
        answer.append(sn)
    
    return answer