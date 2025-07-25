import sys
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)] + [0]

stack = []
answer = 0
for i in range(n + 1):
  num = nums[i]
  while stack and nums[stack[-1]] > num:
    pi = stack.pop()

    if stack:
      width = i - stack[-1] - 1
    else:
      width = i

    answer = max(answer, nums[pi] * width)

  stack.append(i)

print(answer)