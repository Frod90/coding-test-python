import sys
input = sys.stdin.readline

d1 = [[False] * 10 for _ in range(9)]
d2 = [[False] * 10 for _ in range(9)]
d3 = [[[False] * 10 for _ in range(3)] for _ in range(3)]

graph = [list(map(int, list(input().rstrip()))) for _ in range(9)]
blanks = []
for y in range(9):
  for x in range(9):
    if graph[y][x] != 0:
      v = graph[y][x]
      d1[y][v] = True
      d2[x][v] = True
      d3[y // 3][x // 3][v] = True
    else:
      blanks.append((x, y))

def recur(index):
  if index >= len(blanks):
    for row in graph:
      print("".join(map(str, row)))
    exit()

  x, y = blanks[index]
  for v in range(1, 10):
    if not d1[y][v] and not d2[x][v] and not d3[y // 3][x // 3][v]:
      d1[y][v] = True
      d2[x][v] = True
      d3[y // 3][x // 3][v] = True
      graph[y][x] = v
      recur(index + 1)
      graph[y][x] = 0
      d1[y][v] = False
      d2[x][v] = False
      d3[y // 3][x // 3][v] = False

recur(0)