
n = int(input())
nums = list(map(int, input().split()))
answer = [0 for _ in range(n)]
answer[n - 1] = -1
tmp = [nums[-1]]

for i in range(n - 2, -1, -1):

  while tmp:
    if nums[i] >= tmp[-1]:
      tmp.pop()
    else:
      answer[i] = tmp[-1]
      break
  else:
    answer[i] = -1
  
  tmp.append(nums[i])

print(*answer)