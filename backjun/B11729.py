import sys
print = sys.stdout.writelines

n = int(input())
routes = []
def recur(n, s, e, m):

  if n == 1:
    routes.append([s, e])
    return
  
  recur(n - 1, s, m, e)
  routes.append([s, e])
  recur(n - 1, m, e, s)

recur(n, 1, 3, 2)
print(str(len(routes)) + '\n')
for s, e in routes:
  print(str(s) + " " + str(e) + '\n')