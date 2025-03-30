import sys
input = sys.stdin.readline

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]
graph.sort(key=lambda x: (x[1], x[0]))

answers = [graph[0]]
s, e = graph[0][0], graph[0][1]

for i in range(1, n):
  ns, ne =graph[i]

  if e <= ns:
    answers.append([ns, ne])
    e = ne

print(len(answers))