def is_match(key, lock, dx, dy):
    for y in range(len(lock)):
        for x in range(len(lock[0])):
            ky, kx = y - dy, x - dx
            key_value = key[ky][kx] if 0 <= ky < len(key) and 0 <= kx < len(key[0]) else 0
            if lock[y][x] + key_value != 1:
                return False
    return True

def check(key, lock):
    h, w = len(key), len(key[0])
    n = len(lock)
    for dy in range(-h + 1, n):
        for dx in range(-w + 1, n):
            if is_match(key, lock, dx, dy):
                return True 
    return False

def rotate(key):
    h, w = len(key), len(key[0])
    tmp = [[0] * h for _ in range(w)]
    for x in range(w):
        for y in range(h):
            tmp[x][h - 1 - y] = key[y][x]
    return tmp

def solution(key, lock):
    for _ in range(4):
        if check(key, lock):
            return True
        key = rotate(key)
    return False