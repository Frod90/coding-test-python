import sys
from collections import deque
input = sys.stdin.readline

def move(x, y, dx, dy):
  count = 0
  while graph[y + dy][x + dx] != '#':
    x += dx
    y += dy
    count += 1

    if graph[y][x] == 'O':
      break
  
  return x, y, count

def isConductRound(rx, ry, bx, by, moveCount):
  delta = [(0, 1), (0, -1), (-1, 0), (1, 0)]

  for dx, dy in delta:
    nrx, nry, rc = move(rx, ry, dx, dy)
    nbx, nby, bc = move(bx, by, dx, dy)

    if rx == nrx and ry == nry and bx == nbx and by == nby:
      continue

    if graph[nby][nbx] == 'O':
      continue

    if graph[nry][nrx] == 'O':
      return False

    if nrx == nbx and nry == nby:
      if rc < bc:
        nbx -= dx
        nby -= dy
      else:
        nrx -= dx
        nry -= dy
    
    q.append([nrx, nry, nbx, nby, moveCount + 1])

  return True

r, c = map(int, input().split())
graph = []
for y in range(r):
  row = list(input().rstrip())
  graph.append(row)

  for x in range(c):
    if row[x] == 'R':
      R = [x, y]
    if row[x] == 'B':
      B = [x, y]

q = deque()
q.append([R[0], R[1], B[0], B[1], 0])

moveCount = 0
while q:
  rx, ry, bx, by, count = q.popleft()

  if count >= 10 or not isConductRound(rx, ry, bx, by, count):
    moveCount = count + 1
    break

if moveCount <= 10:
  print(moveCount)
else:
  print(-1)