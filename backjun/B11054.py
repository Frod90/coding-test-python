
n = int(input())
nums = list(map(int, input().split()))
dp_inc = [1 for _ in range(n)]
dp_desc = [1 for _ in range(n)]
answer = 0

for i in range(n):

  for j in range(i):
    if nums[i] > nums[j]:
      dp_inc[i] = max(dp_inc[i], dp_inc[j] + 1)
  
for i in range(n - 1, -1, -1):
  for j in range(n - 1, i, -1):
    if nums[i] > nums[j]:
      dp_desc[i] = max(dp_desc[i], dp_desc[j] + 1)

  answer = max(answer, dp_inc[i] + dp_desc[i] - 1)

print(answer)