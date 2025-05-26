
n, m = map(int, input().split())
nums = list(map(int, input().split()))

answer_set = set()
tmp = []

def _recur(d):

  if d == m:
    answer_set.add(tuple(nums[i] for i in tmp))
    return
  
  for j in range(n):
    if j in tmp:
      continue
    tmp.append(j)
    _recur(d + 1)
    tmp.pop()

_recur(0)
for answer in sorted(answer_set):
  print(*answer)