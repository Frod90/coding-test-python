import sys
sys.setrecursionlimit(99999999)

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

whiteCount = 0
blueCount = 0

def _check(x, y, leng):

  defaultSign = graph[y][x]
  for iy in range(y, y + leng):
    for ix in range(x, x + leng):
      if defaultSign != graph[iy][ix]:
        return False

  return True

def _recur(x, y, leng):

  global whiteCount, blueCount

  if _check(x, y, leng):
    if graph[y][x] == 1:
      blueCount += 1
    else:
      whiteCount += 1
    return
  
  el = leng // 2
  for ex, ey in [[0, 0], [el, 0], [0, el], [el, el]]:
    nx, ny = x + ex, y + ey
    _recur(nx, ny, el)

_recur(0, 0, n)
print(whiteCount)
print(blueCount)