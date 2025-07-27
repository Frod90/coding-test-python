import sys
sys.setrecursionlimit(200_000)
input = sys.stdin.readline

def recur(node):
  global id

  visit[node] = True
  id += 1
  ids[node] = id
  minNodeId = id
  stack.append(node)

  for next_node in links[node]:
    if not visit[next_node]:
      minNodeId = min(minNodeId, recur(next_node))
    elif not finished[next_node]:
      minNodeId = min(minNodeId, ids[next_node])

  if minNodeId == ids[node]:
    elements = []
    while stack:
      p = stack.pop()
      finished[p] = True
      elements.append(p)
      
      if node == p:
        break
  
    answers.append(sorted(elements))

  return minNodeId

v, e = map(int, input().split())
links = [[] for _ in range(v + 1)]
for _ in range(e):
  a, b = map(int, input().split())
  links[a].append(b)

stack = []
id = 0
ids = {}
visit = [False] * (v + 1)
finished = [False] * (v + 1)
answers = []
for node in range(1, v + 1):
  if not finished[node]:
     recur(node)

answers.sort()
print(len(answers))
for answer in answers:
  print(*answer, -1)