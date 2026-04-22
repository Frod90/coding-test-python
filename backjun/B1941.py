import sys
input = sys.stdin.readline
from itertools import combinations
from collections import deque

def check_count(candidate):
  count = 0
  for x, y in candidate:
    if graph[y][x] == 'S':
      count += 1
  return count >= 4

def check_surround(candidate):
  candidate_set = set(candidate)
  q = deque()
  q.append(candidate[0])
  s = set()
  s.add(candidate[0])

  while q:
    bx, by = q.popleft()

    for ex, ey in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
      nx, ny = bx + ex, by + ey
      if 0 <= nx < 5 and 0 <= ny < 5 and (nx, ny) in candidate_set and (nx, ny) not in s:
        q.append((nx, ny))
        s.add((nx, ny))
  
  return len(s) == 7

graph = [list(input().rstrip()) for _ in range(5)]
indexs = []
for y in range(5):
  for x in range(5):
    indexs.append((x, y))

answer = 0
for candidate in combinations(indexs, 7):
  if check_count(candidate) and check_surround(candidate):
    answer += 1
print(answer)