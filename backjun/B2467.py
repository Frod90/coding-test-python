
n = int(input())
nums = list(map(int, input().split()))

l, r = 0, n - 1
mini = abs(nums[l] + nums[r])
answer = [nums[l], nums[r]]

while l < r:
  
  tmp = nums[l] + nums[r]

  if tmp == 0:
    answer = [nums[l], nums[r]]
    break
  
  if abs(tmp) < mini:
    answer = [nums[l], nums[r]]
    mini = abs(tmp)

  if tmp < 0:
    l += 1
  else:
    r -= 1

print(*answer)