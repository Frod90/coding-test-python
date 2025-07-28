import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
indexs = []
arr = []

for num in nums:
  index = bisect_left(arr, num)
  indexs.append(index)

  if index == len(arr):
    arr.append(num)
  else:
    arr[index] = num

base = len(arr) - 1
answer = [0] * len(arr)
for i in range(n - 1, -1, -1):
  if base == indexs[i]:
    answer[base] = nums[i]
    base -= 1

print(len(arr))
print(*answer)