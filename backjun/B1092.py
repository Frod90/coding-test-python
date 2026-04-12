import sys
input = sys.stdin.readline

n = int(input())
cranes = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)

if boxes[0] > cranes[0]:
    print(-1)
    exit()

visit = [False] * m
crane_pointers = [0] * n
count = 0
time = 0

while count < m:

  for i in range(n):
    pointer = crane_pointers[i]
    weight = cranes[i]

    while pointer < m:
      if not visit[pointer] and boxes[pointer] <= weight:
        visit[pointer] = True
        count += 1
        pointer += 1
        break
            
      pointer += 1
    crane_pointers[i] = pointer
  
  time += 1

print(time)