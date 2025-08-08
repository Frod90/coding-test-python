import sys
input = sys.stdin.readline

def cal(nums):
  target = 0
  for num in nums:
    if num > target + 1:
      return target + 1
    else:
      target += num
  
  return target + 1

n = int(input())
nums = sorted(list(map(int, input().split())))
print(cal(nums))