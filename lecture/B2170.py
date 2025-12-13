import sys
input = sys.stdin.readline

arr = []
n = int(input())
for _ in range(n):
  a, b = map(int, input().split())
  arr.append((a, b))

arr.sort()
answer = arr[0][1] - arr[0][0]
s = arr[0][1]
for a, b in arr[1:]:
  if a <= s and s < b:
    answer += b - s
    s = b
  if s < a:
    answer += b - a
    s = b

print(answer)