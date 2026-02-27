import sys
input = sys.stdin.readline

n = int(input())
links = [int(input()) - 1 for _ in range(n)]

answer = set()
for i in range(n):
  node = links[i]
  tmp = [i]
  visit = [False] * n
  visit[i] = True

  while not visit[node] and node != i:
    visit[node] = True
    tmp.append(node)
    node = links[node]
    
  if node == i:
    answer.update(tmp)

print(len(answer))
for a in sorted(answer):
  print(a + 1)