answer = [-1] * 11
score_gap = 0

def cal(info, arr):
    a_score = 0
    b_score = 0
    for i in range(10):
        if info[i] == 0 and arr[i] == 0:
            continue
        
        if info[i] < arr[i]:
            a_score += 10 - i
        else:
            b_score += 10 - i
            
    return a_score - b_score

def is_winner(arr, gap):
    global answer, score_gap
    
    if gap == score_gap:
        for i in range(10, -1, -1):
            if answer[i] < arr[i]:
                return True
            elif answer[i] > arr[i]:
                return False
    
    return gap > score_gap    

def recur(n, depth, rest_arrow, info, arr):
    global answer, score_gap
    
    if n == depth:
        arr[depth] = rest_arrow
        gap = cal(info, arr)
        
        if gap > 0 and is_winner(arr, gap):
            answer = arr[:]
            score_gap = gap
        arr[depth] = 0
        return
    
    target_arrow_count = info[depth]
    if target_arrow_count < rest_arrow:
        arr[depth] = target_arrow_count + 1
        recur(n, depth + 1, rest_arrow - target_arrow_count - 1, info, arr)
        arr[depth] = 0
    
    arr[depth] = 0
    recur(n, depth + 1, rest_arrow, info, arr)
    
def solution(n, info):
    recur(10, 0, n, info, [0] * 11)
    if answer[0] == -1:
        return [-1]
    
    return answer