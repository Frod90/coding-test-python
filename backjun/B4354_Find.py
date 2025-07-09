import sys
input = sys.stdin.readline

def cal(p):
  text = '.' + p[1:] + p
  i = text.find(p)
  return len(p) // i

while True:
  p = input().rstrip()
  if p == '.':
    break
  print(cal(p))