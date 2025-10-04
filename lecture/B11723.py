import sys
input = sys.stdin.readline

def _add(bit, a):
  return bit | (1 << a)

def _remove(bit, a):
  return bit & ~(1 << a)

def _check(bit, a):
  return 1 if bit & (1 << a) else 0

def _toggle(bit, a):
  return bit ^ (1 << a)

def _all():
  return (1 << 21) - 2

def _empty():
  return 0

n = int(input())
bit = 0
for _ in range(n):
  s = list(input().rstrip().split(" "))
  if s[0] == "add":
    bit = _add(bit, int(s[1]))
  elif s[0] == "remove":
    bit = _remove(bit, int(s[1]))
  elif s[0] == "check":
    print(_check(bit, int(s[1])))
  elif s[0] == "toggle":
    bit = _toggle(bit, int(s[1]))
  elif s[0] == "all":
    bit = _all()
  elif s[0] == "empty":
    bit = _empty()