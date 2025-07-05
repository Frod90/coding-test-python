import sys
from collections import deque
input = sys.stdin.readline

n, l = map(int, input().split())
nums = list(map(int, input().split()))
q = deque()
answer = []

for i in range(len(nums)):  
  
  miniIndex = i - l
  while q and q[0][1] <= miniIndex:
    q.popleft()

  num = nums[i]
  while q and q[-1][0] >= num:
    q.pop()

  q.append([num, i])
  answer.append(q[0][0])

print(*answer)