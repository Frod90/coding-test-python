
def solution(n):
    def recur(n, a, b, c):
        nonlocal answer
        
        if n == 1:
            answer.append([a, c])
            return
        
        recur(n - 1, a, c, b)
        answer.append([a, c])
        recur(n - 1, b, a, c)

    answer = []
    recur(n, 1, 2, 3)
    return answer