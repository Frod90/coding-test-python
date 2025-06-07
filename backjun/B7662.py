import sys, heapq

input = sys.stdin.readline

t = int(input())

for _ in range(t):

  c = int(input())
  min_q = []
  max_q = []
  visit = [False for _ in range(c)]

  for i in range(c):
    cmd, inputNum = input().split()
    num = int(inputNum)

    if cmd == "I":
      heapq.heappush(min_q, [num, i])
      heapq.heappush(max_q, [-num, i])
      visit[i] = True

    if cmd == "D":
      if num == 1:
        while max_q and not visit[max_q[0][1]]:
          heapq.heappop(max_q)
        
        if max_q:
          tmp, idx = heapq.heappop(max_q)
          visit[idx] = False
        
      elif num == -1:
        while min_q and not visit[min_q[0][1]]:
          heapq.heappop(min_q)
        
        if min_q:
          tmp, idx = heapq.heappop(min_q)
          visit[idx] = False

  while max_q and not visit[max_q[0][1]]:
    heapq.heappop(max_q)
  while min_q and not visit[min_q[0][1]]:
    heapq.heappop(min_q)

  if max_q and min_q:
    print(-max_q[0][0], min_q[0][0])
  else:
    print("EMPTY")
