import sys
sys.setrecursionlimit(9999999)

n = int(input())

visit01 = [0 for _ in range(n)]
visit02 = [0 for _ in range(n * 2)]
visit03 = [0 for _ in range(n * 2)]

def recur(y):

  global count
  
  if y == n:
    count += 1
    return

  for nx in range(n):
    dist02, dist03 = y + nx, y - nx + n - 1

    if visit01[nx] == 0 and visit02[dist02] == 0 and visit03[dist03] == 0:
      visit01[nx], visit02[dist02], visit03[dist03] = 1, 1, 1
      recur(y + 1)
      visit01[nx], visit02[dist02], visit03[dist03] = 0, 0, 0

count = 0
recur(0)
print(count)