def cal(total, count):
  tmp = 1
  division = 1
  count = min(count, total - count)

  for _ in range(count):
    tmp *= total
    division *= count
    total -= 1
    count -= 1
  return tmp // division

n, m, k = map(int, input().split())
if cal(n + m, n) < k:
  print(-1)
  exit()

arr = []
aCount = n
zCount = m
while aCount > 0 and zCount > 0:
  count = cal(aCount + zCount - 1, zCount)
  if k <= count:
    arr.append('a')
    aCount -= 1
  else:
    arr.append('z')
    zCount -= 1
    k -= count

arr += ['a'] * aCount + ['z'] * zCount
print("".join(arr))