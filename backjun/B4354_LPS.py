import sys
input = sys.stdin.readline

def lps(p):
  f = [0] * len(p)
  i, j = 1, 0

  while i < len(p):

    if p[i] == p[j]:
      f[i] = j + 1
      i += 1
      j += 1
    elif j > 0:
      j = f[j - 1]
    else:
      f[i] = 0
      i += 1

  return f

def cal(p):
  f = lps(p)

  l = len(p)
  repeatUnitLength = l - f[-1]
  if l % repeatUnitLength == 0:
    return l // repeatUnitLength
  
  return 1
  
while True:
  p = input().rstrip()
  if p == '.':
    break

  print(cal(p))