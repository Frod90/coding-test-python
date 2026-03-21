import sys
input = sys.stdin.readline

n, l = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def check_x(y):
  visit = [False] * n
  x = 0

  while x < n - 1:
    if graph[y][x + 1] > graph[y][x]:
      if graph[y][x + 1] - graph[y][x] > 1:
        return False
      
      if visit[x]:
        return False
      visit[x] = True
      
      for d in range(1, l):
        cx = x - d
        if cx < 0 or visit[cx] or graph[y][x] != graph[y][cx]:
          return False
        visit[cx] = True
        
    elif graph[y][x + 1] < graph[y][x]:
      if graph[y][x] - graph[y][x + 1] > 1:
        return False
      
      if visit[x + 1]:
        return False
      visit[x + 1] = True
      
      for d in range(2, l + 1):
        cx = x + d
        if n <= cx or visit[cx] or graph[y][x + 1] != graph[y][cx]:
          return False
        visit[cx] = True
      x += l - 1
    
    x += 1

  return True

def check_y(x):
  visit = [False] * n
  y = 0

  while y < n - 1:
    if graph[y + 1][x] > graph[y][x]:
      if graph[y + 1][x] - graph[y][x] > 1:
        return False
      
      if visit[y]:
        return False
      visit[y] = True

      for d in range(1, l):
        cy = y - d
        if cy < 0 or visit[cy] or graph[y][x] != graph[cy][x]:
          return False
        visit[cy] = True
        
    elif graph[y + 1][x] < graph[y][x]:
      if graph[y][x] - graph[y + 1][x] > 1:
        return False
      
      if visit[y + 1]:
        return False
      visit[y + 1] = True
      
      for d in range(2, l + 1):
        cy = y + d
        if n <= cy or visit[cy] or graph[y + 1][x] != graph[cy][x]:
          return False
        visit[cy] = True
      y += l - 1
    
    y += 1

  return True

count = 0
for i in range(n):
  if check_x(i):
    count += 1
  if check_y(i):
    count += 1
print(count)
