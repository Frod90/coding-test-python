import sys
sys.setrecursionlimit(99999999)
input = sys.stdin.readline

v, e = map(int, input().split())

links = [[] for _ in range(v + 1)]
reverse_links = [[] for _ in range(v + 1)]
for _ in range(e):
  a, b = map(int, input().split())
  links[a].append(b)
  reverse_links[b].append(a)

def recur(node):
  for next_node in links[node]:
    if not visit[next_node]:
      visit[next_node] = True
      recur(next_node)
  
  stack.append(node)  

def re_recur(node):
  global elements

  for next_node in reverse_links[node]:
    if not visit[next_node]:
      visit[next_node] = True
      elements.append(next_node)
      re_recur(next_node)

stack = []
visit = [False] * (v + 1)
for i in range(1, v + 1):
  if not visit[i]:
    visit[i] = True
    recur(i)

answers = []
visit = [False] * (v + 1)
while stack:
  p = stack.pop()

  if not visit[p]:
    visit[p] = True
    elements = [p]
    re_recur(p)
    answers.append(sorted(elements))

answers.sort()
print(len(answers))
for answer in answers:
  print(*answer, -1)