import sys
sys.setrecursionlimit(99999999)

n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]

def recur(i, income):

  global answer

  if i >= n:
    if i == n:
      answer = max(answer, income)
    return
  
  recur(i + table[i][0], income + table[i][1])
  recur(i + 1, income)

answer = 0
recur(0, 0)
print(answer)