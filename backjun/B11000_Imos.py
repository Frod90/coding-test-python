import sys
input = sys.stdin.readline

n = int(input())
s = set()
times = []
for _ in range(n):
  a, b = map(int, input().split())
  s.add(a)
  s.add(b)
  times.append([a, b])

comp = {}
for i, num in enumerate(sorted(s)):
  comp[num] = i

arr = [0] * (len(comp))
for a, b in times:
  arr[comp[a]] += 1
  arr[comp[b]] -= 1

for i in range(1, len(arr)):
  arr[i] += arr[i - 1]

print(max(arr))