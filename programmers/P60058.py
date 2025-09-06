def solution(p):
    
    def isCorrect(p):
        count = 0
        for ch in p:
            count += 1 if ch == '(' else -1
            if count < 0:
                return False
        return count == 0
    
    def calSplitLength(p):
        count = 0
        for i, ch in enumerate(p):
            count += 1 if ch == '(' else -1
            if count == 0:
                return i + 1
        
    def _recur(p):
        if p == "":
            return ""
        if isCorrect(p):
            return p

        length = calSplitLength(p)
        u, v = p[:length], _recur(p[length:])
        
        if isCorrect(u):
            return u + v
        else:
            return '(' + v + ')' + "".join('(' if ch == ')' else ')' for ch in p[1:length - 1])
        
    return _recur(p)