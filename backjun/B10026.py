import sys
sys.setrecursionlimit(9999999)

n = int(input())

graph = [list(input()) for _ in range(n)]

visit = [[0 for _ in range(n)] for _ in range(n)]

def recur(x, y, sign, count):

  for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
    nx , ny = x + dx, y + dy

    if 0 <= nx < n and 0 <= ny < n:
      if graph[ny][nx] == sign and visit[ny][nx] == 0:
          visit[ny][nx] = count
          recur(nx, ny, sign, count)

def weakRecur(x, y, count):

  for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
    nx , ny = x + dx, y + dy

    if 0 <= nx < n and 0 <= ny < n:
      if graph[ny][nx] == "R" or graph[ny][nx] == "G":
        if visit[ny][nx] == 0:
          visit[ny][nx] = count
          weakRecur(nx, ny, count)

count = 0
for x in range(n):
  for y in range(n):
    
    if visit[y][x] == 0:
      count += 1
      visit[y][x] = count
      recur(x, y, graph[y][x], count)

visit = [[0 for _ in range(n)] for _ in range(n)]

countWeak = 0
for x in range(n):
  for y in range(n):
    
    if visit[y][x] == 0:
      countWeak += 1
      visit[y][x] = countWeak

      if graph[y][x] == "R" or graph[y][x] == "G":
        weakRecur(x, y, countWeak)
      else: 
        recur(x, y, graph[y][x], countWeak)

print(count, countWeak)
