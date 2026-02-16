import sys
input = sys.stdin.readline

w, c, h = map(int, input().split())
default_crosses = [list(map(int, input().split())) for _ in range(c)]
crosses = [[False] * (w + 1) for _ in range(h + 1)]
for y, x in default_crosses:
  crosses[y][x] = True

def check():
  for x in range(1, w + 1):
    current = x
    for y in range(1, h + 1):
      if crosses[y][current]:
        current += 1
      elif crosses[y][current - 1]:
        current -= 1

    if x != current:
      return False
  return True

def recur(start_y, start_x, depth):
  global answer

  if depth >= answer:
    return
  
  if check():
    answer = depth
    return
  
  if depth == 3:
    return
  
  for x in range(start_x, w):
    if crosses[start_y][x] or crosses[start_y][x - 1] or crosses[start_y][x + 1]:
      continue

    crosses[start_y][x] = True
    recur(start_y, x + 2, depth + 1)
    crosses[start_y][x] = False

  for y in range(start_y + 1, h + 1):
    for x in range(w):
      if crosses[y][x] or crosses[y][x - 1] or crosses[y][x + 1]:
        continue

      crosses[y][x] = True
      recur(y, x + 2, depth + 1)
      crosses[y][x] = False

answer = 4
recur(0, 0, 0)
print(answer if answer < 4 else -1)