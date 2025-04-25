import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for _ in range(t):

  cmds = list(input().rstrip())
  n = int(input())
  arr = input().strip()[1:-1]
  if arr:
    q = deque(map(int, arr.split(',')))
  else:
    q = deque()
  
  isReverse = False
  minIdx = 0
  maxIdx = n - 1
  for cmd in cmds:
    if cmd == 'R':
      isReverse = not isReverse
    if cmd == 'D':

      if not q:
        print("error")
        break

      if isReverse:
        q.pop()
      else:
        q.popleft()
  else:
    if isReverse:
      q.reverse()
    print("[" + ",".join(map(str, q)) + "]")
