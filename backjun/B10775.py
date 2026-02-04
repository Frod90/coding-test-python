import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

g = int(input())
p = int(input())
ps = [int(input()) for _ in range(p)]
parents = [i for i in range(g + 1)]

def find(child):
  if child == parents[child]:
    return child
  parents[child] = find(parents[child])
  return parents[child]

count = 0
for gi in ps:
  parent = find(gi)
  if parent == 0:
    break
  
  parents[parent] = parent - 1
  count += 1

print(count)