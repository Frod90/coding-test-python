import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
k = int(input())
graph = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(k):
  r, c = map(int, input().split())
  graph[r - 1][c - 1] = 1

l = int(input())
cmds = {}
for _ in range(l):
  x, c = input().split()
  cmds[int(x)] = c

directs = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def _calc():

  q = deque()
  q.append([0, 0])
  graph[0][0] = 2
  timeout = 0
  d = 0

  while q:
    x, y = q[-1]
    timeout += 1

    ex, ey = directs[d]
    nx, ny = x + ex, y + ey
    if nx < 0 or n <= nx or ny < 0 or n <= ny or graph[ny][nx] == 2:
      return timeout
    
    if graph[ny][nx] == 0:
      bx, by = q.popleft()
      graph[by][bx] = 0

    graph[ny][nx] = 2
    q.append([nx, ny])

    cmd = cmds.get(timeout, 'S')

    if cmd == 'D':
      d = (d + 1) % 4
    elif cmd == 'L':
      d = (d + 3) % 4

  return timeout

print(_calc())