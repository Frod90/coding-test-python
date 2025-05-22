
n = int(input())
nums = list(map(int, input().split()))
dist = [0 for _ in range(n)]
tmps = [n - 1]

tmpIdx = 0
for i in range(n - 2, -1, -1):

  while tmps:
    idx = tmps[-1]

    if nums[i] > nums[idx]:
      dist[idx] = i + 1
      tmps.pop()
    else:
      break

  tmps.append(i)

print(*dist)