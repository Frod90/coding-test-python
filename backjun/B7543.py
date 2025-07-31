import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
A, B, C, D = [], [], [], []
for _ in range(n):
  a, b, c, d = map(int, input().split())
  A.append(a)
  B.append(b)
  C.append(c)
  D.append(d)

abDict = defaultdict(int)
for i in range(n):
  for j in range(n):
    abDict[A[i] + B[j]] += 1

count = 0
for i in range(n):
  for j in range(n):
    count += abDict.get(-(C[i] + D[j]), 0)

print(count)