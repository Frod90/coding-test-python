import sys
sys.setrecursionlimit(10000)

answer = 0
def solution(n):
    def recur(n, y):
        global answer
        
        if n == y:
            answer += 1
            return

        for x in range(n):
            if not visit01[y - x + n] and not visit02[y + x] and not visit03[x]:
                visit01[y - x + n] = True
                visit02[y + x] = True
                visit03[x] = True
                recur(n, y + 1)
                visit01[y - x + n] = False
                visit02[y + x] = False
                visit03[x] = False
    
    visit01 = [False] * (n * 2)
    visit02 = [False] * (n * 2)
    visit03 = [False] * n
    
    recur(n, 0)
    return answer