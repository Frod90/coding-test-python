import sys

from collections import deque
input = sys.stdin.readline

nums = [deque(list(map(int, list(input().rstrip())))) for _ in range(4)]

t = int(input())
cmds = [list(map(int, input().split())) for _ in range(t)]

def _move(idx, dr):

  if dr == 1:
    a = nums[idx].pop()
    nums[idx].appendleft(a)
  else:
    a = nums[idx].popleft()
    nums[idx].append(a)

for i, d in cmds:

  moveInfos = [[i - 1, d]]

  li = i - 1
  ld = d
  while li > 0:
    if nums[li][6] != nums[li - 1][2]:
      li = li - 1
      ld = -ld
      moveInfos.append([li, ld])
    else:
      break

  ri = i - 1
  rd = d
  while ri < 3:
    if nums[ri][2] != nums[ri + 1][6]:
      ri = ri + 1
      rd = -rd
      moveInfos.append([ri, rd])
    else:
      break

  for idx, dr in moveInfos:
    _move(idx, dr)

answer = 0
if nums[0][0] == 1:
  answer += 1
if nums[1][0] == 1:
  answer += 2
if nums[2][0] == 1:
  answer += 4
if nums[3][0] == 1:
  answer += 8

print(answer)