
n, s = map(int, input().split())
nums = list(map(int, input().split()))

answer = n * 2

tmpSum = 0
j = 0
for i in range(n):
  tmpSum += nums[i]

  while tmpSum >= s and j <= i:
    answer = min(answer, i - j + 1)

    tmpSum -= nums[j]
    j += 1

if answer == n * 2:
  print(0)
else:
  print(answer)