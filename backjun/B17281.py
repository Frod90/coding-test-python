import sys
input = sys.stdin.readline
from itertools import permutations

def cal(entry):
  entry_index = 0
  score = 0
  for y in range(n):
    count = 0
    b1, b2, b3 = 0, 0, 0

    while count < 3:
      v = graph[y][entry[entry_index]]
      if v == 0:
        count += 1
      elif v == 1:
        score += b3
        b3 = b2
        b2 = b1
        b1 = 1
      elif v == 2:
        score += b3 + b2
        b3 = b1
        b2 = 1
        b1 = 0
      elif v == 3:
        score += b3 + b2 + b1
        b3 = 1
        b2, b1 = 0, 0
      elif v == 4:
        score += b3 + b2 + b1 + 1
        b3, b2, b1 = 0, 0, 0
        
      entry_index = (entry_index + 1) % 9
        
  return score

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
players = [i for i in range(1, 9)]
answer = 0
for p in permutations(players):
  p = list(p)
  entry = p[:3] + [0] + p[3:]
  answer = max(answer, cal(entry))

print(answer)