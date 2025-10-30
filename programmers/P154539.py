def solution(numbers):
    answer = [-1] * len(numbers)
    s = []
    
    for i, num in enumerate(numbers):
        while s and s[-1][0] < num:
            _, index = s.pop()
            answer[index] = num
        s.append((num, i))
    
    return answer