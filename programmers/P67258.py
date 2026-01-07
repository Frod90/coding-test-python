from collections import defaultdict

def solution(gems):
    n = len(set(gems))
    d = defaultdict(int)
    
    left = 0
    answer = [0, len(gems)]
    for right, gem in enumerate(gems):
        d[gem] += 1
        
        while len(d) == n:
            d[gems[left]] -= 1
            if d[gems[left]] == 0:
                del d[gems[left]]
                if answer[1] - answer[0] > right - left:
                    answer = [left + 1, right + 1]
            left += 1
    
    return answer