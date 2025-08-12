import sys
input = sys.stdin.readline

def canMove(x, y, c):
  if c == 'h' and x < n - 1 and graph[y][x + 1] == 0:
    return True
  if c == 'v' and y < n - 1 and graph[y + 1][x] == 0:
    return True
  if c == 'd' and x < n - 1 and y < n - 1 and graph[y + 1][x] == 0 and graph[y][x + 1] == 0 and graph[y + 1][x + 1] == 0:
    return True

  return False

def recur(x, y, c):

  if canMove(x, y, 'd'):
    dist[y + 1][x + 1] += 1
    recur(x + 1, y + 1, 'd')

  if c == 'h':
    if canMove(x, y, 'h'):
      dist[y][x + 1] += 1
      recur(x + 1, y, 'h')

  if c == 'v':
    if canMove(x, y, 'v'):
      dist[y + 1][x] += 1
      recur(x, y + 1, 'v')

  if c == 'd':
    if canMove(x, y, 'h'):
      dist[y][x + 1] += 1
      recur(x + 1, y, 'h')
    if canMove(x, y, 'v'):
      dist[y + 1][x] += 1
      recur(x, y + 1, 'v')

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dist = [[0] * n for _ in range(n)]

recur(1, 0, 'h')
print(dist[-1][-1])