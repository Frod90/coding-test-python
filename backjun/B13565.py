import sys
sys.setrecursionlimit(9999999)

h, w = map(int, input().split())

graph = [list(map(int, input().rstrip())) for _ in range(h)]
visit = [[0 for _ in range(w)] for _ in range(h)]

def recur(x, y):

  for ex, ey in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
    nx, ny = x + ex, y + ey

    if 0 <= nx < w and 0 <= ny < h:
      if graph[ny][nx] == 0 and visit[ny][nx] == 0:
        visit[ny][nx] = 1
        recur(nx, ny)

for i in range(w):
  if graph[0][i] == 0 and visit[0][i] == 0:
    recur(i, 0)

if 1 in visit[h - 1]:
  print("YES")
else:
  print("NO")
