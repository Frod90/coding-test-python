import sys
input = sys.stdin.readline

s = input().rstrip()
p = input().rstrip()

def failFunction(p):
  f = [0] * len(p)
  j = 0

  for i in range(1, len(p)):

    while j > 0 and p[i] != p[j]:
      j = f[j - 1]

    if p[i] == p[j]:
      f[i] = j + 1
      j += 1
  
  return f

def _KMP(s, p, f):
  pi = 0

  for si in range(len(s)):

    while pi > 0 and s[si] != p[pi]:
      pi = f[pi - 1]

    if s[si] == p[pi]:
      pi += 1

    if pi == len(p):
      return 1
  
  return 0

f = failFunction(p)
print(_KMP(s, p, f))