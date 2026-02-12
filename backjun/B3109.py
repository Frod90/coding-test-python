import sys
input = sys.stdin.readline
sys.setrecursionlimit(10_001)

h, w = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(h)]
visit = [[False] * w for _ in range(h)]
delta = [-1, 0, 1]

def recur(x, y):
  if x == w - 1:
    return True
  
  for ey in delta:
    ny = y + ey
    nx = x + 1
    if 0 <= ny < h and graph[ny][nx] == '.' and not visit[ny][nx]:
      visit[ny][nx] = True
      if recur(nx, ny):
        return True

  return False

answer = 0
for y in range(h):
  if recur(0, y):
    answer += 1

print(answer)