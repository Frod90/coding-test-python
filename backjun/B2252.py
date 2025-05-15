import sys

sys.setrecursionlimit(99999999)
input = sys.stdin.readline

n, m = map(int, input().split())

links = [[] for _ in range(n + 1)]
for _ in range(m):
  a, b = map(int, input().split())
  links[b].append(a)

answers = []
visit = [False for _ in range(n + 1)]

def _calc(i):

  if visit[i]:
    return

  for ni in links[i]:

    if visit[ni]:
      continue
    
    _calc(ni)

  visit[i] = True
  answers.append(i)

for i in range(1, n + 1):
  _calc(i)
print(*answers)