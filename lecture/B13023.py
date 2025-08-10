import sys
input = sys.stdin.readline

def recur(i, count):
  if count == 4:
    return True
  
  for ni in links[i]:
    if not visit[ni]:
      visit[ni] = True
      if recur(ni, count + 1):
        return True
      visit[ni] = False

  return False

n, m = map(int, input().split())
links = [[] for _ in range(n)]
for _ in range(m):
  a, b = map(int, input().split())
  links[a].append(b)
  links[b].append(a)

for i in range(n):
  visit = [False] * n
  visit[i] = True
  if recur(i, 0):
    print(1)
    exit()

print(0)