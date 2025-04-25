import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):

  cmds = list(input().rstrip())
  n = int(input())
  arr = input().strip()[1:-1]
  if arr:
    arr = list(map(int, arr.split(',')))
  else:
    arr =[]
  
  isReverse = False
  minIdx = 0
  maxIdx = n - 1
  for cmd in cmds:
    if cmd == 'R':
      isReverse = not isReverse
    if cmd == 'D':

      if minIdx >= n or maxIdx < 0:
        print("error")
        break

      if isReverse:
        maxIdx -= 1
      else:
        minIdx += 1
  else:
    if isReverse:
      print("[" + ",".join(map(str, arr[minIdx:maxIdx + 1][::-1])) + "]")
    else:
      print("[" + ",".join(map(str, arr[minIdx:maxIdx + 1])) + "]")
