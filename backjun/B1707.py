import sys
from collections import deque

input = sys.stdin.readline

def is_answer():
  v, e = map(int, input().split())

  nodes = [0 for _ in range(v + 1)]
  links = [[] for _ in range(v + 1)]
  for _ in range(e):
    a, b = map(int, input().split())
    links[a].append(b)
    links[b].append(a)

  for i in range(1, v + 1):

    if nodes[i] != 0:
      continue

    q = deque()
    q.append(i)
    nodes[i] = 1

    while q:
      bi = q.popleft()

      for ni in links[bi]:
        if nodes[ni] == 0:
          nodes[ni] = -nodes[bi]
          q.append(ni)
        elif nodes[ni] == nodes[bi]:
          return False
  return True

t = int(input())  

for _ in range(t):
  if is_answer():
    print("YES")
  else:
    print("NO")
