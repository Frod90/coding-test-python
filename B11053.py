
n = int(input())
numbers = list(map(int, input().split()))

visit = [1]*n

for i in range(n):
    for j in range(i):
      if numbers[j] < numbers[i]:
        visit[i] = max(visit[i], visit[j] + 1)

print(max(visit))