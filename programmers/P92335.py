
def toBase(num, n):
    if num == 0:
        return "0"
    
    digits = []
    while num > 0:
        digits.append(str(num % n))
        num //= n
    return "".join(digits[::-1])

def isPrime(num):
    if num < 2:
        return False
    
    for division in range(2, int(num**0.5) + 1):
        if num % division == 0:
            return False    
    return True

def solution(n, k):    
    num_base_k = toBase(n, k)
    answer = 0
    
    for candidate in num_base_k.split("0"):
        if candidate and isPrime(int(candidate)):
            answer += 1
    
    return answer