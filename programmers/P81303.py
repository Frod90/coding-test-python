def solution(n, k, cmd):
    def u(pointer, count):
        for _ in range(count):
            pointer = pre[pointer]
        return pointer
    
    def d(pointer, count):
        for _ in range(count):
            pointer = nex[pointer]
        return pointer
    
    def c(pointer):
        deleted.append((pointer, pre[pointer], nex[pointer]))
        if pre[pointer] >= 0:
            nex[pre[pointer]] = nex[pointer]
        if nex[pointer] < n:
            pre[nex[pointer]] = pre[pointer]
        if nex[pointer] == n:
            return pre[pointer]
        return nex[pointer]
    
    def r():
        pointer, pre_pointer, nex_pointer = deleted.pop()
        
        if pre_pointer >= 0:
            nex[pre_pointer] = pointer
        if nex_pointer < n:
            pre[nex_pointer] = pointer
        
    pre = [i - 1 for i in range(n)]
    nex = [i + 1 for i in range(n)]
    deleted = []
    
    pointer = k
    for infos in cmd:
        info = infos.split(" ")
        if info[0] == 'U':
            pointer = u(pointer, int(info[1]))
        elif info[0] == 'D':
            pointer = d(pointer, int(info[1]))
        elif info[0] == 'C':
            pointer = c(pointer)
        else:
            r()
            
    answer = ['O'] * n
    for pointer, _, _ in deleted:
        answer[pointer] = 'X'
    return ''.join(answer)