import sys
input = sys.stdin.readline

h, w = map(int, input().split())
graph = []
cctvs = []
for y in range(h):
  row = list(map(int, input().split()))
  for x in range(w):
    if 0 < row[x] < 6:
      cctvs.append((row[x], x, y))
  graph.append(row)

d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
directs = []
def add_directs(x, y, cmd, direct):
  directs.append((x, y, d[direct]))

  if cmd == 2:
    directs.append((x, y, d[(direct + 2) % 4]))
  elif cmd == 3:
    directs.append((x, y, d[(direct + 1) % 4]))
  elif cmd == 4:
    directs.append((x, y, d[(direct + 1) % 4]))
    directs.append((x, y, d[(direct + 2) % 4]))
  elif cmd == 5:
    directs.append((x, y, d[(direct + 1) % 4]))
    directs.append((x, y, d[(direct + 2) % 4]))
    directs.append((x, y, d[(direct + 3) % 4]))

def pop_directs(cmd):
  directs.pop()
  if cmd == 2 or cmd == 3:
    directs.pop()
  elif cmd == 4:
    directs.pop()
    directs.pop()
  elif cmd == 5:
    directs.pop()
    directs.pop()
    directs.pop()

def cal():
  g = [row[:] for row in graph]

  for x, y, (ex, ey) in directs:
    nx, ny = x, y
    while 0 <= nx < w and 0 <= ny < h and g[ny][nx] != 6:
      g[ny][nx] = 1
      nx += ex
      ny += ey

  return sum(row.count(0) for row in g)

def recur(index):
  global answer

  if index == len(cctvs):
    answer = min(answer, cal())
    return
  
  cmd, x, y = cctvs[index]
  if cmd == 5:
    add_directs(x, y, cmd, 0)
    recur(index + 1)
    pop_directs(cmd)
  elif cmd == 2:
    for i in range(2):
      add_directs(x, y, cmd, i)
      recur(index + 1)
      pop_directs(cmd)
  else:
    for i in range(4):
      add_directs(x, y, cmd, i)
      recur(index + 1)
      pop_directs(cmd)

answer = h * w
recur(0)
print(answer)