import sys
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]
stack = []

count = 0
for num in nums:
  while stack and stack[-1][0] < num:
    p = stack.pop()

    if stack:
      count += p[1]

    count += p[1]
    count += p[1] * (p[1] - 1) // 2
  
  if stack and stack[-1][0] == num:
    stack[-1][1] += 1 
  else:
    stack.append([num, 1])

while stack:
  p = stack.pop()

  if stack:
    count += p[1]

  count += p[1] * (p[1] - 1) // 2

print(count)