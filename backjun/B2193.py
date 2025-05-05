
n = int(input())

if n > 2: 
  dist = [0 for _ in range(n + 1)]
  dist[1] = 1
  dist[2] = 1

  for i in range(3, n + 1):
    dist[i] = dist[i - 1] + dist[i - 2]

  print(dist[-1])
  
else:
  print(1)