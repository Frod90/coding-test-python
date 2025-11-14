
def solution(citations):
    citations.sort(reverse = True)
    
    answer = 0
    for i, v in enumerate(citations):
        tmp = min(i + 1, v)
        answer = max(answer, tmp)
    
    return answer