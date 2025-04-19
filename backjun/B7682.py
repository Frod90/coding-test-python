import sys

input = sys.stdin.readline

def _check(graph):

  countA = graph.count("X")
  countB = graph.count("O")

  if countA < countB or countA - countB > 1:
    return False

  tmp = set()
  
  for a, b, c in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
    if graph[a] != "." and graph[a] == graph[b] == graph[c]:
      if graph[a] == "O" and countA > countB:
         return False
      
      if graph[a] == "X" and countA == countB:
        return False
      
      tmp.update([a, b, c])
    
    if len(tmp) > 5:
      return False

  if not tmp and countA + countB < 9:
    return False

  return True

while True:

  cmd = input().strip()

  if cmd == "end":
    break

  graph = list(cmd)

  if _check(graph):
    print("valid")
  else:
    print("invalid")