import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n, m = map(int, input().split())
employees = [[]]

for _ in range(n):
  info = list(map(int, input().split()))
  employees.append(info[1:])

def _recur(em):
  for w in employees[em]:
    if visit[w]:
      continue

    visit[w] = True

    if works[w] == 0 or _recur(works[w]):
      works[w] = em
      return True

  return False

works = [0] * (m + 1)
count = 0
for i in range(1, n + 1):
  visit = [False] * (m + 1)
  if _recur(i):
    count += 1

print(count)