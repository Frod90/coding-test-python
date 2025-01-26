import sys
sys.setrecursionlimit(9999999)

from collections import deque

n = int(input())
graph = [[] for _ in range(n)]

for _ in range(n):
  a, b, c = input().split()
  a, b, c = ord(a) - ord("A"), ord(b) - ord("A"), ord(c) - ord("A")
  graph[a].append(b)
  graph[a].append(c)

frontNodes = []
def front(i):

  frontNodes.append(i)

  for next in graph[i]:
    if next >= 0:
      front(next)

front(0)
for a in frontNodes:
  print(chr(a + ord("A")), end="")
print()

midNodes = deque()
def mid(i):

  a, b = graph[i]

  if a >= 0:
    mid(a)
  
  midNodes.append(i)

  if b >= 0:
    mid(b)

mid(0)
for a in midNodes:
  print(chr(a + ord("A")), end="")
print()

backNodes = []
def back(i):

  for next in graph[i]:
    if next >= 0:
      back(next)

  backNodes.append(i)

back(0)
for a in backNodes:
  print(chr(a + ord("A")), end="")
