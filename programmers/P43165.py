import sys
sys.setrecursionlimit(2**20)

def solution(numbers, target):
    
    def recur(result, index, numbers, target):
        nonlocal answer
        
        if index == len(numbers):
            if result == target:
                answer += 1
            return
        
        recur(result + numbers[index], index + 1, numbers, target)
        recur(result - numbers[index], index + 1, numbers, target)
            
    answer = 0
    recur(0, 0, numbers, target)
    return answer