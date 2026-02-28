import sys
input = sys.stdin.readline
sys.setrecursionlimit(10_000)

h, w = map(int, input().split())

graph = [[-1] * w for _ in range(h)]
for y in range(h):
  row = list(input().rstrip())
  for x in range(w):
    if row[x] == 'H':
      continue
    graph[y][x] = int(row[x])

dists = [[-1] * w for _ in range(h)]
visit = [[False] * w for _ in range(h)]
directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def recur(x, y):
  if x < 0 or w <= x or y < 0 or h <= y:
    return 0
  if graph[y][x] == -1:
    return 0
  if visit[y][x]:
    print(-1)
    exit()
  if dists[y][x] != -1:
    return dists[y][x]

  visit[y][x] = True
  
  for ex, ey in directs:
    nx, ny = x + ex * graph[y][x], y + ey * graph[y][x]
    dists[y][x] = max(dists[y][x], recur(nx, ny) + 1)
  
  visit[y][x] = False
  return dists[y][x]

print(recur(0, 0))