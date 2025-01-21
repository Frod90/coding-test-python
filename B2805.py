import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

a, b = 0, max(trees)

answer = 0
while a <= b:

  mid = (a + b)//2

  tmp = 0
  for tree in trees:
    if tree > mid:
      tmp += (tree - mid)

  if tmp == m:
    answer = mid
    break
  elif tmp < m:
    b = mid - 1
  elif tmp > m:
    a = mid + 1
    answer = mid

print(answer)