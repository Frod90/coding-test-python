import sys
input = sys.stdin.readline

def make_word(x, y, word, depth):
  if depth == 6:
    return

  for ex, ey in directs:
    nx, ny = (x + ex) % w, (y + ey) % h
    next_word = word + graph[ny][nx]
    d[next_word] = d.get(next_word, 0) + 1
    make_word(nx, ny, next_word, depth + 1)

h, w, k = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(h)]
words = [input().rstrip() for _ in range(k)]

d = dict()
directs = [[1, 0], [-1, 0], [0, 1], [0, -1], [-1, -1], [1, 1], [-1, 1], [1, -1]]
for y in range(h):
  for x in range(w):
    d[graph[y][x]] = d.get(graph[y][x], 0) + 1
    make_word(x, y, graph[y][x], 1)

for word in words:
  print(d.get(word, 0))