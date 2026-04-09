import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
nums.sort()

count = 0
for i in range(n - 2):
  base = nums[i]
  
  left, right = i + 1, n - 1
  while left < right:
    sum = base + nums[left] + nums[right]

    if sum < 0:
      left += 1
    elif sum > 0:
      right -= 1
    else :
      if nums[left] == nums[right]:
        size = right - left + 1
        count += (size * (size - 1)) // 2
        break
      
      else:
        left_value = nums[left]
        left_count = 0
        while nums[left] == left_value:
          left += 1
          left_count += 1

        right_value = nums[right]
        right_count = 0
        while nums[right] == right_value:
          right -= 1
          right_count += 1

        count += left_count * right_count

print(count)