
def _gcd(a, b):
    a, b = min(a, b), max(a, b)
    while b % a != 0:
        a, b = b % a, a
    return a

def solution(arr):
    answer = 1
    for num in arr:
        g = _gcd(answer, num)
        answer = (answer // g) * (num // g) * g
    
    return answer