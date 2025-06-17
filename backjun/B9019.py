import sys
from collections import deque

input = sys.stdin.readline

def _D(value):
  return (value * 2) % 10_000

def _S(value):
  if value == 0:
    return 9999
  return value - 1

def _L(value):
  a = value // 1000
  b = value // 100 - a * 10
  c = value // 10 - a * 100 - b * 10
  d = value - a * 1000 - b * 100 - c * 10

  return b * 1000 + c * 100 + d * 10 + a

def _R(value):
  a = value // 1000
  b = value // 100 - a * 10
  c = value // 10 - a * 100 - b * 10
  d = value - a * 1000 - b * 100 - c * 10

  return d * 1000 + a * 100 + b * 10 + c

def _cal(value, target):

  visit = [False] * 10_001
  prev = [0] * 10_001
  cmds = [0] * 10_001

  q = deque()
  q.append(value)
  visit[value] = True

  while q:
    bv = q.popleft()

    if bv == target:
      break
    
    for cmd, func in [['D', _D], ['S', _S], ['L', _L], ['R', _R]]:
      nv = func(bv)
      if not visit[nv]:
        q.append(nv)
        visit[nv] = True
        prev[nv] = bv
        cmds[nv] = cmd

  start, end = value, target
  result = []
  while start != end:
    result.append(cmds[end])
    end = prev[end]
   
  return "".join(reversed(result))

t = int(input())
for _ in range(t):
  value, target = map(int, input().split())
  print(_cal(value, target))
