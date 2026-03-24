import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
directs = [
  (0, 0), 
  (-1, 0), (-1, -1), (0, -1), (1, -1),
  (1, 0), (1, 1), (0, 1), (-1, 1)
  ]
diagonal = [(-1, -1), (1, -1), (1, 1), (-1, 1)]
move = [list(map(int, input().split())) for _ in range(m)]

cloud = [[0, n - 1], [0, n - 2], [1, n - 1], [1, n - 2]]
for d, s in move:

  for i in range(len(cloud)):
    ex, ey = directs[d]
    nx = (cloud[i][0] + ex * s) % n
    ny = (cloud[i][1] + ey * s) % n
    
    cloud[i][0], cloud[i][1] = nx, ny
    graph[ny][nx] += 1

  tmp_arr = []
  for x, y in cloud:
    tmp_value = 0
    for ex, ey in diagonal:
      nx, ny = x + ex, y + ey
      if 0 <= nx < n and 0 <= ny < n and graph[ny][nx] > 0:
        tmp_value += 1
    if tmp_value > 0:
      tmp_arr.append((x, y, tmp_value))
  for x, y, ev in tmp_arr:
    graph[y][x] += ev

  cloud.sort()
  next_cloud = []
  index = 0
  for x in range(n):
    for y in range(n):
      if index < len(cloud) and x == cloud[index][0] and y == cloud[index][1]:
        index += 1
        continue

      if graph[y][x] >= 2:
        next_cloud.append([x, y])
        graph[y][x] -= 2
  cloud = next_cloud

answer = sum(sum(row) for row in graph)
print(answer)