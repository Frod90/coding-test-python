import sys
sys.setrecursionlimit(500000)
input = sys.stdin.readline

n, m = map(int, input().split())
owners = [[] for _ in range(n + 1)]
for _ in range(m):
  a, b = map(int, input().split())
  owners[a].append(b)

def _recur(owner):
  if visit[owner]:
    return False
  visit[owner] = True

  for laptop in owners[owner]:
    if laptops[laptop] == -1 or _recur(laptops[laptop]):
      laptops[laptop] = owner
      return True

  return False

count = 0
laptops = [-1] * (n + 1)
for i in range(1, n + 1):
  visit = [False] * (n + 1)
  if _recur(i):
    count += 1

  if count == n:
    break

print(count)