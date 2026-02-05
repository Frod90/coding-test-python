import sys
input = sys.stdin.readline

n = 19
graph = [list(map(int, input().split())) for _ in range(n)]

def check(x, y, ex, ey):
  count = 1
  lx, ly = x + ex, y + ey
  while 0 <= lx < n and 0 <= ly < n:
    if graph[ly][lx] != graph[y][x]:
      break

    count += 1
    lx += ex
    ly += ey
    if count > 5:
      break
  
  rx, ry = x - ex, y - ey
  while 0 <= rx < n and 0 <= ry < n:
    if graph[ry][rx] != graph[y][x]:
      break

    count += 1
    rx -= ex
    ry -= ey
    if count > 5:
      break

  return count == 5

def s():
  directs = [(1, 0), (0, 1), (1, 1), (1, -1)]

  for y in range(n):
    for x in range(n):
      for ex, ey in directs:
        if graph[y][x] == 0:
          continue

        if check(x, y, ex, ey):
          lx, ly = x, y
          while 0 <= lx and 0 <= ly < n and graph[ly][lx] == graph[y][x]:
            lx -= ex
            ly -= ey
          print(graph[y][x])
          print(ly + ey + 1, lx + ex + 1)
          return
  
  print(0)
  return
s()