from itertools import permutations

def solution(numbers):
    arr = [False] * 10_000_000
    arr[0] = True
    arr[1] = True
    for i in range(2, int(10_000_000**0.5) + 1):
        if not arr[i]:
            for j in range(i * 2, 10_000_000, i):
                arr[j] = True
    
    nums = list(numbers)
    s = set()
    for i in range(1, len(nums) + 1):
        for digits in permutations(nums, i):
            s.add(int("".join(digits)))
    
    answer = 0
    for num in s:
        if not arr[num]:
            answer += 1
    return answer