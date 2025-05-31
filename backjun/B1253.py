
n = int(input())
nums = list(map(int, input().split()))
nums.sort()

def _isAnswer(idx):

  l, r = 0, n - 1

  while l < r:

    if l == idx:
      l += 1
      continue
    if r == idx:
      r -= 1
      continue

    tmp = nums[l] + nums[r]

    if tmp == nums[idx]:
      return True
    
    if tmp < nums[idx]:
      l += 1
    elif tmp > nums[idx]:
      r -= 1

  return False

count = 0
for i in range(n):
  if _isAnswer(i):
    count += 1
print(count)