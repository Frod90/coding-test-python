import sys
input = sys.stdin.readline

n = int(input())
base, compare = map(int, input().split())
m = int(input())

parent = [i for i in range(n + 1)]

for _ in range(m):

  a, b = map(int, input().split())
  parent[b] = a

def _find(a):

  nodes = []
  nodes.append(a)

  while a != parent[a]:

    nodes.append(parent[a])
    a = parent[a]

  return nodes

baseList = _find(base)

compareCount = 0
answer = -1
while True:

  isEnd = False
  for i in range(len(baseList)):
    if baseList[i] == compare:
      answer = compareCount + i
      isEnd = True
      break

  if isEnd or compare == parent[compare]:
    break
  compare = parent[compare]
  compareCount += 1

print(answer)