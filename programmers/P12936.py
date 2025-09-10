from math import factorial

def solution(n, k):
    answer = []
    nums = [i for i in range(1, n + 1)]
    k -= 1
    
    for degree in range(n, 0, -1):
        base = factorial(degree - 1)
        answer.append(nums.pop(k // base))
        k %= base
    
    return answer