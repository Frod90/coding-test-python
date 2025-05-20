import sys

input = sys.stdin.readline

n, c = map(int, input().split())
nodes = [int(input()) for _ in range(n)]
nodes.sort()

def _isPossible(mid):

  count = 1
  bi = 0
  for i in range(1, n):
    if nodes[i] - nodes[bi] >= mid:
      bi = i
      count += 1

    if count >= c:
      return True
  
  return False

mini, maxi = 1, nodes[-1] - nodes[0]
answer = 0

while mini <= maxi:

  mid = (mini + maxi) // 2
  if _isPossible(mid):
    answer = mid
    mini = mid + 1
  else:
    maxi = mid - 1

print(answer)