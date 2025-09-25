def solution(number, k):
    nums = list(map(int, list(number)))
    s = []
    
    for num in nums:
        while s and k > 0 and s[-1] < num:
            k -= 1
            s.pop()
        
        s.append(num)
        
    if k > 0:
        s = s[:-k]

    return "".join(list(map(str, s)))