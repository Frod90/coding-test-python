import sys
sys.setrecursionlimit(99999999)

n = int(input())
linkCount = int(input())

graph = [[] for i in range(n + 1)]

for i in range(linkCount):
  a, b = map(int, input().split())
  
  graph[a].append(b)
  graph[b].append(a)

visit = [0] * (n + 1)
visit[1] = 1

def recur(i):

  global count

  for j in graph[i]:
    if visit[j] == 0:
      visit[j] = 1
      count += 1
      recur(j)

count = 0
recur(1)
print(count)