import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
lis = []
indexs = []

for num in nums:
  index = bisect_left(lis, num)
  if index == len(lis):
    lis.append(num)
  else:
    lis[index] = num
  indexs.append(index)

answer = []
count = len(lis) - 1
for i in range(n - 1, -1, -1):
  if indexs[i] != count:
    continue
  
  count -= 1
  answer.append(nums[i])
answer.sort()

print(len(lis))
print(*answer)