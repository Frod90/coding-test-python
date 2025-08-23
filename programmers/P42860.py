def solution(name):
    answer = 0
    
    base = ord('A')
    diff = ord('Z') + 1
    for n in name:
        nc = ord(n)
        c = min(nc - base, diff - nc)
        answer += c
    
    length = len(name)
    move = length - 1
    for i in range(length):
        idx = i + 1
        while idx < length and name[idx] == 'A':
            idx += 1
        
        option01 = i * 2 + (length - idx)
        option02 = (length - idx) * 2 + i
        move = min(move, option01, option02)
    
    return answer + move