import sys

sys.setrecursionlimit(9999999)
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
answers = [0, 0, 0]

def _match(sx, ex, sy, ey, base):

  for y in range(sy, ey):
    for x in range(sx, ex):
      if graph[y][x] != base:
        return False
      
  return True

def _recur(sx, ex, sy, ey, l):

  base = graph[sy][sx]
  if _match(sx, ex, sy, ey, base):
    answers[base + 1] += 1
    return
  
  nl01, nl02 = l//3, 2*(l//3)

  nxts = [
    [sx, sx + nl01, sy, sy + nl01],
    [sx + nl01, sx + nl02, sy, sy + nl01],
    [sx + nl02, ex, sy, sy + nl01],

    [sx, sx + nl01, sy + nl01, sy + nl02],
    [sx + nl01, sx + nl02, sy + nl01, sy + nl02],
    [sx + nl02, ex, sy + nl01, sy + nl02],

    [sx, sx + nl01, sy + nl02, ey],
    [sx + nl01, sx + nl02, sy + nl02, ey],
    [sx + nl02, ex, sy + nl02, ey],
    ]
  
  for nsx, nex, nsy, ney in nxts:
    _recur(nsx, nex, nsy, ney, l//3)

_recur(0, n, 0, n, n)
for answer in answers:
  print(answer)