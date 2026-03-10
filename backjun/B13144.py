import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
nums = list(map(int, input().split()))
d = defaultdict(int)
answer = 0
length = 0
remove_left = 0

for i, num in enumerate(nums):
  if d.get(num, -1) != -1:
    remove_right = d[num]

    for j in range(remove_left, remove_right + 1):
      d[nums[j]] = -1
      length -= 1
    remove_left = remove_right + 1

  d[num] = i
  length += 1
  answer += length

print(answer)