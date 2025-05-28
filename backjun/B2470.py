
n = int(input())
nums = list(map(int, input().split()))
nums.sort()

l, r = 0, n - 1
tmp = nums[l] + nums[r]
mini = nums[l] + nums[r]
answer = [nums[l], nums[r]]

while l < r:

  tmp = nums[l] + nums[r]

  if tmp == 0:
    answer = [nums[l], nums[r]]
    break

  if abs(tmp) < abs(mini):
    answer = [nums[l], nums[r]]
    mini = tmp

  if tmp > 0:
    r -= 1
  elif tmp < 0:
    l += 1

print(*answer)