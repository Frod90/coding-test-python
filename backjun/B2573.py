import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
infos = []
for y in range(n):
  row = list(map(int, input().split()))
  graph.append(row)
  for x in range(m):
    if row[x] != 0:
      infos.append([x, y, row[x]])

def _sync():
  for x, y, v in infos:
    graph[y][x] = v

def _deduct():
  for i in range(len(infos)):
    x, y, v = infos[i]

    count = 0
    for ex, ey in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
      nx, ny = x + ex, y + ey 
      if 0 <= nx < m and 0 <= ny < n:
        if graph[ny][nx] == 0:
          count += 1
    infos[i][2] = max(0, v - count)

def _isContinue():

  if not infos:
    return False

  q = deque()
  q.append((infos[0][0], infos[0][1]))

  visit = [[False for _ in range(m)] for _ in range(n)]
  visit[infos[0][1]][infos[0][0]] = True

  count = 1

  while q:
    x, y = q.popleft()
    for ex, ey in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
      nx, ny = x + ex, y + ey 
      if 0 <= nx < m and 0 <= ny < n:
        if graph[ny][nx] > 0 and not visit[ny][nx]:
          count += 1
          q.append((nx, ny))
          visit[ny][nx] = True

  return count == len(infos)

answer = 0
while _isContinue():
  answer += 1
  _deduct()
  _sync()
  infos = [info for info in infos if info[2] > 0]

if infos:
  print(answer)
else:
  print(0)