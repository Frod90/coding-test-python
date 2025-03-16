import sys
sys.setrecursionlimit(99999999)

h, w = map(int, input().split())

graph = [list(input()) for _ in range(h)]
visit = [[0 for _ in range(w)] for _ in range(h)]

def recur(x, y):

  global count

  for ex, ey in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
    nx, ny = x + ex, y + ey

    if 0 <= nx < w and 0 <= ny < h:
      if graph[ny][nx] != "X" and visit[ny][nx] == 0:

        if graph[ny][nx] == "P":
          count += 1

        visit[ny][nx] = 1
        recur(nx, ny)
        

for x in range(w):
  for y in range(h):

    if graph[y][x] == "I":
      count = 0
      visit[y][x] = 1
      recur(x, y)
      break

if count == 0:
  print("TT")
else:
  print(count)