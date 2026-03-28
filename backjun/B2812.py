import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, list(input().rstrip())))

st = []
for num in nums:
  while st and k > 0 and st[-1] < num:
    st.pop()
    k -= 1
  
  st.append(num)

for _ in range(k):
  st.pop()

print(int("".join(map(str, st))))