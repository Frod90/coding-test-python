import sys
input = sys.stdin.readline
from itertools import combinations

w, c, h = map(int, input().split())
default_crosses = [list(map(int, input().split())) for _ in range(c)]
crosses = [[False] * (w + 1) for _ in range(h + 1)]
for y, x in default_crosses:
  crosses[y][x] = True

def is_a(extra_cross):
  for y, x in extra_cross:
    if crosses[y][x + 1] or crosses[y][x - 1]:
      for y, x in extra_cross:
        crosses[y][x] = False
      return False
    
    crosses[y][x] = True
  
  for x in range(1, w + 1):
    mx = x
    for y in range(1, h + 1):
      if crosses[y][mx]:
        mx += 1
      elif crosses[y][mx - 1]:
        mx -= 1
    
    if mx != x:
      for y, x in extra_cross:
        crosses[y][x] = False
      return False
    
  return True

def cal():
  candidates = [
    [y, x] for y in range(1, h + 1) for x in range(1, w) 
    if not crosses[y][x] and not crosses[y][x + 1] and not crosses[y][x - 1]
    ]
  for extra_count in range(4):
    for extra_cross in combinations(candidates, extra_count):
      if is_a(extra_cross):
        return extra_count  
  return -1

print(cal())