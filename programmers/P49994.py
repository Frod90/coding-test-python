def move(x, y, d):
    if d == 'U' and y < 5:
        return x, y + 1
    if d == 'D' and y > -5:
        return x, y - 1
    if d == 'R' and x < 5:
        return x + 1, y
    if d == 'L' and x > -5:
        return x - 1, y
    return x, y

def solution(dirs):
    s = set()
    x, y = 0, 0
    for d in dirs:
        nx, ny = move(x, y, d)
        if x == nx and y == ny:
            continue
        s.add((min(x, nx), min(y, ny), max(x, nx), max(y, ny)))
        x, y = nx, ny
        
    return len(s)

a = 'a'
a.isalpha