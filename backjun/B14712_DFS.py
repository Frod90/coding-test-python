h, w = map(int, input().split())
graph = [[0] * w for _ in range(h)]

def recur(x, y):
  global count

  if y == h:
    count += 1
    return
  
  nx, ny = (x + 1, y) if x < w - 1 else (0, y + 1)
  recur(nx, ny)

  if x >= 1 and y >= 1 and graph[y - 1][x - 1] and graph[y - 1][x] and graph[y][x - 1]:
    return
  
  graph[y][x] = 1
  recur(nx, ny)
  graph[y][x] = 0

count = 0
recur(0, 0)
print(count)