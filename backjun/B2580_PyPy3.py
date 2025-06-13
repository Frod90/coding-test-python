import sys
sys.setrecursionlimit(10000)
input =  sys.stdin.readline

graph = []
blanks = []

for y in range(9):

  row = list(map(int, input().split()))
  graph.append(row)

  for x in range(9):
    if row[x] == 0:
      blanks.append([x, y])

def _is_possible(x, y, v):

  for i in range(9):
    if graph[y][i] == v or graph[i][x] == v:
      return False

  tx, ty = x // 3 * 3, y // 3 * 3
  for i in range(ty, ty + 3):
    for j in range(tx, tx + 3):
      if graph[i][j] == v:
        return False
  
  return True

def _recur(depth):

  if depth == len(blanks):
    for row in graph:
      print(*row)
    sys.exit(0)

  x, y = blanks[depth]
  for j in range(1, 10):
    if _is_possible(x, y, j):
      graph[y][x] = j
      _recur(depth + 1)
      graph[y][x] = 0

_recur(0)