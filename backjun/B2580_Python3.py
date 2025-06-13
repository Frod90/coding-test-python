import sys
sys.setrecursionlimit(10000)
input =  sys.stdin.readline

graph = []
blanks = []

row_sets = [set() for _ in range(9)]
col_sets = [set() for _ in range(9)]
box_sets = [set() for _ in range(9)]

def get_box_index(x, y):
  return y // 3 * 3 + x // 3

for y in range(9):

  row = list(map(int, input().split()))
  graph.append(row)

  for x in range(9):

    num = row[x]

    if num == 0:
      blanks.append([x, y])
    else:
      row_sets[x].add(num)
      col_sets[y].add(num)
      box_sets[get_box_index(x, y)].add(num)

def _recur(depth):
  if depth == len(blanks):
    for row in graph:
      print(*row)
    sys.exit(0)

  x, y = blanks[depth]
  b = get_box_index(x, y)

  for num in range(1, 10):
    if num not in row_sets[x] and num not in col_sets[y] and num not in box_sets[b]:
      graph[y][x] = num
      row_sets[x].add(num)
      col_sets[y].add(num)
      box_sets[b].add(num)

      _recur(depth + 1)

      row_sets[x].remove(num)
      col_sets[y].remove(num)
      box_sets[b].remove(num)

_recur(0)