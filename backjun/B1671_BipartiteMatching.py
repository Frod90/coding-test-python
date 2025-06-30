import sys
sys.setrecursionlimit(99999999)
input = sys.stdin.readline

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
s.sort(key=lambda x: (x[0], x[1], x[2]))

def can_eat(i, j):
  if s[i][0] >= s[j][0] and s[i][1] >= s[j][1] and s[i][2] >= s[j][2]:
    if s[i][0] == s[j][0] and s[i][1] == s[j][1] and s[i][2] == s[j][2]:
      return i > j
    return True

  return False

eatable = [[] for _ in range(n)]
for i in range(n):
  for j in range(i):
    if can_eat(i, j):
      eatable[i].append(j)

def _recur(i):
  for j in eatable[i]:
    if visit[j]:
      continue

    visit[j] = True

    if result[j] == -1 or _recur(result[j]):
      result[j] = i
      return True

  return False

result = [-1] * n
count = 0
for i in range(n):
  for j in range(2):
    visit = [False] * n

    if _recur(i):
      count += 1

print(n - count)