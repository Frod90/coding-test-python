import sys
input = sys.stdin.readline

n = int(input())
graph = [int(input()) for _ in range(n)]

answers = []
s = []
idx = 0
for i in range(1, n + 1):

  s.append(i)
  answers.append("+")

  while s and idx < n and s[-1] == graph[idx]:
    s.pop()
    answers.append("-")
    idx += 1

if len(s) == 0:
  for answer in answers:
    print(answer)
else:
  print("NO")
