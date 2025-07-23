import sys
import heapq
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) + [i] for i in range(n)]

x_sort = sorted(graph, key=lambda x:(x[0]))
y_sort = sorted(graph, key=lambda x:(x[1]))
z_sort = sorted(graph, key=lambda x:(x[2]))

links = [[] for _ in range(n)]
for i in range(n - 1):
  x, y, z, index = x_sort[i]
  nx, ny, nz, nindex = x_sort[i + 1]
  value = nx - x
  links[index].append([nindex, value])
  links[nindex].append([index, value])

  x, y, z, index = y_sort[i]
  nx, ny, nz, nindex = y_sort[i + 1]
  value = ny - y
  links[index].append([nindex, value])
  links[nindex].append([index, value])

  x, y, z, index = z_sort[i]
  nx, ny, nz, nindex = z_sort[i + 1]
  value = nz - z
  links[index].append([nindex, value])
  links[nindex].append([index, value])

visit = [False] * n
q = [[0, 0]]
answer = 0
count = 0

while q:
  if count == n:
    break

  bv, bi = heapq.heappop(q)

  if not visit[bi]:
    visit[bi] = True
    answer += bv
    count += 1

    for ni, nv in links[bi]:
      heapq.heappush(q, [nv, ni])
    
print(answer)