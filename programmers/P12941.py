def solution(A,B):
    A.sort()
    B.sort(key=lambda x:-x)
    
    answer = 0
    for i in range(len(A)):
        answer += A[i] * B[i]
    return answer