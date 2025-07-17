import sys
input = sys.stdin.readline

def cal(n, nums):
  arr = []
  a = 0

  for i in range(n):
    
    while arr and nums[arr[-1]] > nums[i]:
      j = arr.pop()
      if arr:
        w = i - arr[-1] - 1
      else:
        w = i
      a = max(a, nums[j] * w)

    arr.append(i)

  while arr:
    j = arr.pop()
    if arr:
      w = n - arr[-1] - 1
    else:
      w = n
    a = max(a, nums[j] * w)

  return a

while True:
  nums = list(map(int, input().split()))
  if nums[0] == 0:
    break

  print(cal(nums[0], nums[1:]))