from functools import cmp_to_key

def compare(a, b):
    if a + b > b + a:
        return -1
    if a + b < b + a:
        return 1
    return 0
    
def solution(numbers):    
    nums = list(map(str, numbers))
    nums.sort(key=cmp_to_key(compare))
    if nums[0] == "0":
        return "0"
    return "".join(nums)