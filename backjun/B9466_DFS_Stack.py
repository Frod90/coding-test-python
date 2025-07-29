import sys
sys.setrecursionlimit(200_000)
input = sys.stdin.readline

def recur(node):
  global count

  visit[node] = True
  stack.append(node)

  next_node = links[node]
  if not visit[next_node]:
    recur(next_node)
    return

  tmpCount = 0
  base = links[stack[-1]]
  while stack:
    p = stack.pop()
    tmpCount += 1

    if p == base:
      count += tmpCount
      return
  
t = int(input())
for _ in range(t):
  n = int(input())
  links = [0] + list(map(int, input().split()))

  visit = [False] * (n + 1)
  count = 0
  for node in range(1, n + 1):
    if not visit[node]:
      stack = []
      recur(node)

  print(n - count)