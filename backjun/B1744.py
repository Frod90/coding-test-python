import sys
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]

answer = 0
nums.sort()
while len(nums) >= 2:
  if nums[-1] <= 1 or nums[-2] <= 1:
    break
  answer += nums.pop() * nums.pop()

nums.sort(key=lambda x:-x)
while len(nums) >= 2:
  if nums[-1] > 0 or nums[-2] > 0:
    break
  answer += nums.pop() * nums.pop()

for num in nums:
  answer += num
print(answer)