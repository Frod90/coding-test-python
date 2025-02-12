import sys
input = sys.stdin.readline

sys.setrecursionlimit(99999999)

t = int(input())

for i in range(t):
  columnCount, rowCount, count = map(int, input().split())
  graph = [[0 for _ in range(columnCount)] for _ in range(rowCount)]
  visit = [[0 for _ in range(columnCount)] for _ in range(rowCount)]

  for j in range(count):
    x, y = map(int, input().split())
    graph[y][x] = 1
    
  def recursion(x, y):
    
    visit[y][x] = 1

    for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
      nx, ny = x + dx, y + dy

      if 0 <= nx < columnCount and 0 <= ny < rowCount and graph[ny][nx] == 1 and visit[ny][nx] == 0:
        recursion(nx, ny)

  answer = 0
  for x in range(columnCount):
    for y in range(rowCount):
      
      if graph[y][x] == 1 and visit[y][x] == 0:
        answer += 1
        recursion(x, y)
  
  print(answer)