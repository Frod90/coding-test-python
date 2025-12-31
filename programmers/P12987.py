
def solution(A, B):
    A.sort(key=lambda x:-x)
    B.sort()
    
    left, right = 0, len(B) - 1
    answer = 0
    for a in A:
        if a >= B[right]:
            left += 1
        else:
            answer += 1
            right -= 1
            
    return answer