import sys
input = sys.stdin.readline

n = int(input())
p = input().rstrip()

f = [0] * n
i = 1
j = 0

while i < n:

  if p[i] == p[j]:
    f[i] = j + 1
    i += 1
    j += 1
  elif j > 0:
    j = f[j - 1]
  else:
    f[i] = j
    i += 1

print(n - f[-1])