import sys
input = sys.stdin.readline

n = int(input())
p = input().rstrip()

f = [0] * n
j = 0

for i in range(1, n):  
  while j > 0 and p[i] != p[j]:
    j = f[j - 1]

  if p[i] == p[j]:
    f[i] = j + 1
    j += 1

print(n - f[-1])