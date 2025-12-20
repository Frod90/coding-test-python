import sys
input = sys.stdin.readline

n = int(input())
nums = sorted(list(map(int, input().split())))

answer = []
sum_value = 3_000_000_000
k = n - 1
while k >= 2 and sum_value != 0:
  base = nums[k]
  
  i, j = 0, k - 1
  while i < j:
    candidate = base + nums[i] + nums[j]

    if sum_value > abs(candidate):
      answer = [base, nums[i], nums[j]]
      sum_value = abs(candidate)

      if sum_value == 0:
        break
      
    if candidate < 0:
      i += 1
    else:
      j -= 1
      
  k -= 1

print(*sorted(answer))