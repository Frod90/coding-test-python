import sys
sys.setrecursionlimit(10000)

def _recur(s, count):
    if s == 0:
        return count
    if s == 1:
        return count + 1
    
    d = s % 10
    ns = s // 10
    return min(_recur(ns, count + d), _recur(ns + 1, count + 10 - d))
        
def solution(storey):
    return _recur(storey, 0)