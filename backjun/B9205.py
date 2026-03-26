import sys
input = sys.stdin.readline
from collections import deque

t = int(input())
for _ in range(t):
  n = int(input())
  base_x, base_y = map(int, input().split())
  conveniences = [list(map(int, input().split())) for _ in range(n)]
  target_x, target_y = map(int, input().split())

  visit = [False] * n
  q = deque()
  q.append((base_x, base_y))
  answer = "sad"
  while q:
    current_x, current_y = q.popleft()
    if abs(current_x - target_x) + abs(current_y - target_y) <= 1000:
      answer = "happy"
      break

    for i, (next_x, next_y) in enumerate(conveniences):
      if not visit[i]:
        if abs(current_x - next_x) + abs(current_y - next_y) <= 1000:
          visit[i] = True
          q.append((next_x, next_y))
  
  print(answer)