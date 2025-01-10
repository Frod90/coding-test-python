import sys
input = sys.stdin.readline

n, h = map(int, input().split())

line = [0 for _ in range(h)]

for i in range(n):
  height = int(input())

  if(i % 2 == 0):
    line[0] += 1
    line[height] -= 1

  if(i % 2 != 0):
    line[h - height] += 1

for i in range(h - 1):
  line[i + 1] = line[i + 1] + line[i]

minCount = min(line)

# userCount = 0
# for count in line:
#   if(count == minCount):
#     userCount += 1

print(minCount, line.count(minCount))