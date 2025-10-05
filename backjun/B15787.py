import sys
input = sys.stdin.readline

def _add(bit, i):
  return bit | (1 << i)

def _remove(bit, i):
  return bit & ~(1 << i)

def _right(bit):
  bit >>= 1
  return bit & (((1 << 21) - 1) & ~1)

def _left(bit):
  bit <<= 1
  return bit & ((1 << 21) - 1)

n, m = map(int, input().split())
graph = [0] * (n + 1)

for _ in range(m):
  c = list(map(int, input().split()))

  if c[0] == 1:
    graph[c[1]] = _add(graph[c[1]], c[2])
  elif c[0] == 2:
    graph[c[1]] = _remove(graph[c[1]], c[2])
  elif c[0] == 3:
    graph[c[1]] = _left(graph[c[1]])
  elif c[0] == 4:
    graph[c[1]] = _right(graph[c[1]])

print(len(set(graph[1:])))