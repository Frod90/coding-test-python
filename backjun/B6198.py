import sys
input = sys.stdin.readline

n = int(input())
heights = [int(input()) for _ in range(n)]

st = []
answer = 0
for i, h in enumerate(heights):
  while st and st[-1][1] <= h:
    bi, _ = st.pop()
    answer += i - bi - 1

  st.append((i, h))

while st:
  bi, _ = st.pop()
  answer += n - bi - 1

print(answer)