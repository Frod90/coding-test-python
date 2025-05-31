
strs = list(input().strip())
base = list(input().strip())
n = len(base)
s = []

def _isAnswer():

  if len(s) < n:
    return False
  
  for i in range(n):
    if base[i] != s[-n + i]:
      return False

  return True

def _extract():
  for _ in range(n):
    s.pop()

for i in range(len(strs)):
  s.append(strs[i])
  while _isAnswer():
    _extract()

if s:
  print("".join(s))
else:
  print("FRULA")