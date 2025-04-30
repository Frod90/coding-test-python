import sys

sys.setrecursionlimit(99999999)
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, list(input().rstrip()))) for _ in range(n)]

def _check(sx, ex, sy, ey):

  defaultNum = graph[sy][sx]

  for y in range(sy, ey):
    for x in range(sx, ex):
      if graph[y][x] != defaultNum:
        return False
      
  return True

def _recur(sx, ex, sy, ey, leng):

  global answer

  if _check(sx, ex, sy, ey):
    answer += str(graph[sy][sx])
    return
  
  nxtLeng = leng // 2
  answer += "("

  for nsx, nex, nsy, ney in [
    [sx, sx + nxtLeng, sy, sy + nxtLeng], [sx + nxtLeng, ex, sy, sy + nxtLeng],
    [sx, sx + nxtLeng, sy + nxtLeng, ey], [sx + nxtLeng, ex, sy + nxtLeng, ey],
    ]:

    _recur(nsx, nex, nsy, ney, nxtLeng)

  answer += ")"

answer = ""
_recur(0, n, 0, n, n)
print(answer)