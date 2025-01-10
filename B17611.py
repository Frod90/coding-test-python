import sys
input = sys.stdin.readline

n = int(input())

limit = 500_000

xGraph = [0 for _ in range(1001000)]
yGraph = [0 for _ in range(1001000)]

tmpX, tmpY = map(int, input().split())
tmpX += limit
tmpY += limit
initX, initY = tmpX, tmpY

for i in range(1, n):
  x, y = map(int, input().split())
  x += limit
  y += limit

  if tmpX == x:
    yGraph[min(tmpY, y)] += 1
    yGraph[max(tmpY, y)] -= 1
  
  if tmpY == y:
    xGraph[min(tmpX, x)] += 1
    xGraph[max(tmpX, x)] -= 1

  tmpX, tmpY = x, y

if tmpX == initX:
    yGraph[min(tmpY, initY)] += 1
    yGraph[max(tmpY, initY)] -= 1
elif tmpY == initY:
    xGraph[min(tmpX, initX)] += 1
    xGraph[max(tmpX, initX)] -= 1

for i in range(1, 1001000):
    xGraph[i] = xGraph[i] + xGraph[i - 1]
    yGraph[i] = yGraph[i] + yGraph[i - 1]

print(max(max(xGraph), max(yGraph)))
