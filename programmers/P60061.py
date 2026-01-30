def solution(n, build_frame):
    def can(x, y, a):
        if a == 0:
            return (
                y == 0 or
                (x, y - 1, 0) in s or
                (x - 1, y, 1) in s or
                (x, y, 1) in s
            )

        return (
            (x, y - 1, 0) in s or
            (x + 1, y - 1, 0) in s or
            ((x - 1, y, 1) in s and (x + 1, y, 1) in s)
        )
    
    def valid():
        for x, y, a in s:
            if not can(x, y, a):
                return False
        return True
    
    s = set()
    for x, y, a, b in build_frame:
        if b:
            s.add((x, y, a))
            if not valid():
                s.remove((x, y, a))
        else:
            s.remove((x, y, a))
            if not valid():
                s.add((x, y, a))
    return sorted(s)